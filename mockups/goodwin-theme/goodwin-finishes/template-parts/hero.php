<?php
/**
 * Homepage hero.
 *
 * Copy lives here rather than in the editor — it changes rarely, and keeping
 * it out of a page builder is the point of this theme. Edit the text below.
 *
 * @package goodwin
 */

// The hero image is the newest featured project's main image.
$gw_hero = new WP_Query(
	array(
		'post_type'      => 'project',
		'posts_per_page' => 1,
		'meta_key'       => '_thumbnail_id',
		'meta_query'     => array(
			array(
				'key'     => 'featured',
				'value'   => '1',
				'compare' => '=',
			),
		),
	)
);

if ( ! $gw_hero->have_posts() ) {
	$gw_hero = new WP_Query(
		array(
			'post_type'      => 'project',
			'posts_per_page' => 1,
			'meta_key'       => '_thumbnail_id',
		)
	);
}
?>

<section class="hero">
	<div class="hero__type">
		<p class="label">Decorative wall finishes · Newcastle &amp; Port Stephens</p>
		<h1>Turning walls into <em>Works of Art</em></h1>
		<p class="hero__sub lede">Hand-troweled microcement, Venetian plaster and lime wash for builders, interior designers and homeowners across Newcastle.</p>

		<div class="hero__cta">
			<a class="btn btn--solid" href="#contact">Book a free quote</a>
			<a class="btn" href="#work">See the work</a>
		</div>

		<div class="hero__meta">
			<div><b>2018</b><span class="label">Studio founded</span></div>
			<div><b><?php echo esc_html( wp_count_posts( 'project' )->publish ); ?></b><span class="label">Projects</span></div>
			<?php // Placeholder figure — confirm with Lauren before launch. ?>
			<div><b>200+</b><span class="label">Walls finished</span></div>
		</div>
	</div>

	<?php
	if ( $gw_hero->have_posts() ) :
		while ( $gw_hero->have_posts() ) :
			$gw_hero->the_post();
			?>
			<figure class="hero__img">
				<?php the_post_thumbnail( 'gw-full', array( 'fetchpriority' => 'high' ) ); ?>
				<figcaption class="hero__caption">
					<?php echo esc_html( trim( gw_primary_term() . ' · ' . gw_field( 'location' ), ' ·' ) ); ?>
				</figcaption>
			</figure>
			<?php
		endwhile;
		wp_reset_postdata();
	endif;
	?>
</section>
