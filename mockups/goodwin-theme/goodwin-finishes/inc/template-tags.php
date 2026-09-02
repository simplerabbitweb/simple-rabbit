<?php
/**
 * Template helpers.
 *
 * @package goodwin
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Read an ACF field without fataling when ACF is inactive.
 *
 * @param string   $name    Field name.
 * @param int|null $post_id Post ID, defaults to current post.
 * @return mixed Field value, or empty string.
 */
function gw_field( $name, $post_id = null ) {
	if ( ! function_exists( 'get_field' ) ) {
		return '';
	}

	$value = get_field( $name, $post_id );

	return ( null === $value || false === $value ) ? '' : $value;
}

/**
 * Space-separated list of a project's finish slugs, for the JS filters.
 *
 * @param int|null $post_id Post ID.
 * @return string
 */
function gw_term_slugs( $post_id = null ) {
	$terms = get_the_terms( $post_id ? $post_id : get_the_ID(), 'project_category' );

	if ( ! $terms || is_wp_error( $terms ) ) {
		return '';
	}

	return implode( ' ', wp_list_pluck( $terms, 'slug' ) );
}

/**
 * First finish term name, used as the tile's caption.
 *
 * @param int|null $post_id Post ID.
 * @return string
 */
function gw_primary_term( $post_id = null ) {
	$terms = get_the_terms( $post_id ? $post_id : get_the_ID(), 'project_category' );

	if ( ! $terms || is_wp_error( $terms ) ) {
		return '';
	}

	return $terms[0]->name;
}

/**
 * One grid tile. Expects to run inside the loop.
 *
 * Not a link and not a button — the gallery is the whole experience, so a tile
 * has nowhere to go.
 *
 * @param bool $wide Render as a two-column tile.
 */
function gw_tile( $wide = false ) {
	if ( ! has_post_thumbnail() ) {
		return;
	}

	$location = gw_field( 'location' );
	$term     = gw_primary_term();
	$caption  = trim( $term . ( $location ? ' · ' . $location : '' ), ' ·' );
	?>
	<figure class="tile<?php echo $wide ? ' tile--wide' : ''; ?>" data-cats="<?php echo esc_attr( gw_term_slugs() ); ?>">
		<?php
		the_post_thumbnail(
			'gw-grid',
			array(
				'loading' => 'lazy',
				'alt'     => esc_attr( get_the_title() . ( $caption ? ' — ' . $caption : '' ) ),
			)
		);
		?>
		<figcaption class="tile__veil">
			<b><?php the_title(); ?></b>
			<?php if ( $caption ) : ?>
				<span><?php echo esc_html( $caption ); ?></span>
			<?php endif; ?>
		</figcaption>
	</figure>
	<?php
}

/**
 * The filter row. Only lists finishes that actually have projects.
 *
 * @param int $total Number of projects in the grid.
 */
function gw_filter_row( $total ) {
	$terms = get_terms(
		array(
			'taxonomy'   => 'project_category',
			'hide_empty' => true,
		)
	);

	if ( is_wp_error( $terms ) || count( $terms ) < 2 ) {
		return;
	}
	?>
	<div class="filters" id="filters">
		<button data-filter="all" aria-pressed="true">All</button>
		<?php foreach ( $terms as $term ) : ?>
			<button data-filter="<?php echo esc_attr( $term->slug ); ?>" aria-pressed="false">
				<?php echo esc_html( $term->name ); ?>
			</button>
		<?php endforeach; ?>
		<span class="count" id="count" data-singular="project" data-plural="projects">
			<?php echo esc_html( $total . ' ' . _n( 'project', 'projects', $total, 'goodwin' ) ); ?>
		</span>
	</div>
	<?php
}

/**
 * Newest project image in a given finish, for the finish cards.
 *
 * @param string $slug Term slug.
 * @return int Attachment ID, or 0.
 */
function gw_term_image( $slug ) {
	$posts = get_posts(
		array(
			'post_type'      => 'project',
			'posts_per_page' => 1,
			'meta_key'       => '_thumbnail_id',
			'tax_query'      => array(
				array(
					'taxonomy' => 'project_category',
					'field'    => 'slug',
					'terms'    => $slug,
				),
			),
		)
	);

	return $posts ? (int) get_post_thumbnail_id( $posts[0]->ID ) : 0;
}

/**
 * Inline an SVG from the theme's assets so it can take its colour from CSS.
 *
 * @param string $file Filename inside assets/img/.
 * @return string Markup, or an empty string if it isn't there.
 */
function gw_svg( $file ) {
	static $cache = array();

	if ( ! isset( $cache[ $file ] ) ) {
		$path            = get_template_directory() . '/assets/img/' . basename( $file );
		$cache[ $file ] = file_exists( $path ) ? file_get_contents( $path ) : ''; // phpcs:ignore WordPress.WP.AlternativeFunctions
	}

	return $cache[ $file ];
}

/**
 * The logo, inlined so it inherits the theme colour rather than shipping as a
 * fixed-black image that would disappear on a dark background.
 *
 * Upload a Custom Logo in the Customizer to override it.
 */
function gw_logo() {
	if ( has_custom_logo() ) {
		the_custom_logo();
		return;
	}

	$svg = gw_svg( 'logo.svg' );

	if ( $svg ) {
		echo $svg; // phpcs:ignore WordPress.Security.EscapeOutput -- bundled theme asset.
	} else {
		echo '<b>' . esc_html( get_bloginfo( 'name' ) ) . '</b>';
	}
}
