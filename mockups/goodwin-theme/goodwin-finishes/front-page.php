<?php
/**
 * Homepage.
 *
 * @package goodwin
 */

get_header();

get_template_part( 'template-parts/hero' );
get_template_part( 'template-parts/intro' );
get_template_part( 'template-parts/finishes' );

/**
 * This is a single-page site, so the homepage grid is the whole gallery —
 * every project with an image, filtered in place rather than on an archive.
 * The "Show on homepage" field now only decides which project supplies the
 * hero image.
 */
$gw_home = new WP_Query(
	array(
		'post_type'      => 'project',
		'posts_per_page' => -1,
		'meta_key'       => '_thumbnail_id',
		'orderby'        => array( 'menu_order' => 'ASC', 'date' => 'DESC' ),
	)
);
?>

<section class="work wrap" id="work">
	<div class="work__head reveal">
		<div>
			<p class="label">Selected projects</p>
			<h2>Every wall, up close</h2>
		</div>
		<p class="lede" style="max-width:34ch;margin:0">Filter by finish to see one kind of work at a time.</p>
	</div>

	<?php gw_filter_row( $gw_home->post_count ); ?>

	<div class="grid" id="grid">
		<?php
		$gw_i = 0;
		while ( $gw_home->have_posts() ) :
			$gw_home->the_post();
			// Every fifth tile runs two columns wide, to break the rhythm.
			gw_tile( 0 === $gw_i % 5 && $gw_i > 0 );
			$gw_i++;
		endwhile;
		wp_reset_postdata();
		?>
	</div>

	<div class="work__more">
		<a class="btn" href="#contact">Enquire about a similar finish</a>
	</div>
</section>

<?php
get_template_part( 'template-parts/about' );
get_template_part( 'template-parts/testimonials' );

get_footer();
