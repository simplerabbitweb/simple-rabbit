<?php
/**
 * Project custom post type + finish taxonomy.
 *
 * @package goodwin
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * The Project post type — one entry per job, with a gallery of photos.
 */
function gw_register_project_cpt() {
	register_post_type(
		'project',
		array(
			'labels'        => array(
				'name'               => 'Projects',
				'singular_name'      => 'Project',
				'add_new'            => 'Add project',
				'add_new_item'       => 'Add new project',
				'edit_item'          => 'Edit project',
				'new_item'           => 'New project',
				'view_item'          => 'View project',
				'search_items'       => 'Search projects',
				'not_found'          => 'No projects yet',
				'not_found_in_trash' => 'No projects in the bin',
				'all_items'          => 'All projects',
				'featured_image'     => 'Main image',
				'set_featured_image' => 'Set main image',
				'menu_name'          => 'Projects',
			),
			// Projects are edited in the admin but have no front-end URL of
			// their own — the whole site is one page, and a project opens in
			// the lightbox there.
			'public'              => false,
			'publicly_queryable'  => false,
			'exclude_from_search' => true,
			'show_ui'             => true,
			'show_in_menu'        => true,
			'has_archive'         => false,
			'menu_icon'     => 'dashicons-format-gallery',
			'menu_position' => 5,
			'supports'      => array( 'title', 'editor', 'thumbnail', 'excerpt', 'page-attributes' ),
			'rewrite'             => false,
			'show_in_rest'        => true,
		)
	);

	register_taxonomy(
		'project_category',
		'project',
		array(
			'labels'            => array(
				'name'          => 'Finishes',
				'singular_name' => 'Finish',
				'add_new_item'  => 'Add finish',
				'menu_name'     => 'Finishes',
			),
			// Used to filter the gallery in place; no term archives.
			'public'             => false,
			'publicly_queryable' => false,
			'show_ui'            => true,
			'hierarchical'       => true,
			'show_admin_column'  => true,
			'show_in_rest'       => true,
			'rewrite'            => false,
		)
	);
}
add_action( 'init', 'gw_register_project_cpt' );

/**
 * Seed the finish terms on first run so the filter row is populated.
 */
function gw_seed_terms() {
	if ( get_option( 'gw_terms_seeded' ) ) {
		return;
	}

	$terms = array(
		'microcement' => 'Microcement',
		'venetian'    => 'Venetian / Marmorino',
		'limewash'    => 'Lime wash',
		'faux'        => 'Decorative / Faux',
		'commercial'  => 'Commercial',
	);

	foreach ( $terms as $slug => $name ) {
		if ( ! term_exists( $slug, 'project_category' ) ) {
			wp_insert_term( $name, 'project_category', array( 'slug' => $slug ) );
		}
	}

	update_option( 'gw_terms_seeded', 1 );
}
add_action( 'after_switch_theme', 'gw_seed_terms', 20 );

/* ─────────────────────────  Admin list table  ───────────────────────── */

/**
 * Add a thumbnail and location column so the list reads like a contact sheet.
 *
 * @param array $columns Existing columns.
 * @return array
 */
function gw_project_columns( $columns ) {
	$new = array();

	foreach ( $columns as $key => $label ) {
		if ( 'title' === $key ) {
			$new['gw_thumb'] = 'Image';
		}
		$new[ $key ] = $label;

		if ( 'title' === $key ) {
			$new['gw_location'] = 'Location';
			$new['gw_featured'] = 'Featured';
		}
	}

	return $new;
}
add_filter( 'manage_project_posts_columns', 'gw_project_columns' );

/**
 * Fill the custom columns.
 *
 * @param string $column  Column key.
 * @param int    $post_id Post ID.
 */
function gw_project_column_content( $column, $post_id ) {
	if ( 'gw_thumb' === $column ) {
		echo has_post_thumbnail( $post_id )
			? get_the_post_thumbnail( $post_id, array( 70, 70 ), array( 'style' => 'object-fit:cover;width:70px;height:70px;' ) )
			: '<span style="color:#b32d2e">No image</span>';
	}

	if ( 'gw_location' === $column ) {
		echo esc_html( gw_field( 'location', $post_id ) );
	}

	if ( 'gw_featured' === $column ) {
		echo gw_field( 'featured', $post_id ) ? '★' : '—';
	}
}
add_action( 'manage_project_posts_custom_column', 'gw_project_column_content', 10, 2 );

/**
 * Widen the thumbnail column a little.
 */
function gw_admin_column_css() {
	$screen = get_current_screen();

	if ( $screen && 'edit-project' === $screen->id ) {
		echo '<style>.column-gw_thumb{width:90px}.column-gw_featured{width:70px;text-align:center}</style>';
	}
}
add_action( 'admin_head', 'gw_admin_column_css' );
