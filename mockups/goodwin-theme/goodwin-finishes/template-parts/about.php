<?php
/**
 * About Lauren. Pulls its copy and image from the "About" page if one exists,
 * so she can edit it in the editor; otherwise falls back to the text below.
 *
 * @package goodwin
 */

$gw_about    = get_page_by_path( 'about' );
$gw_about_id = $gw_about ? $gw_about->ID : 0;
?>

<section class="about" id="about">
	<div class="wrap about__grid">
		<div class="about__img reveal">
			<?php
			if ( $gw_about_id && has_post_thumbnail( $gw_about_id ) ) {
				echo get_the_post_thumbnail( $gw_about_id, 'gw-full', array( 'loading' => 'lazy' ) );
			} else {
				// Set a featured image on the About page to replace this.
				printf(
					'<img src="%s" alt="Lauren Goodwin, decorative painter, Newcastle" loading="lazy">',
					esc_url( get_template_directory_uri() . '/assets/img/lauren-goodwin.jpg' )
				);
			}
			?>
		</div>

		<div class="reveal">
			<p class="label">About Lauren</p>
			<h2>An artist's hand, a tradesperson's preparation</h2>

			<?php if ( $gw_about_id && get_post_field( 'post_excerpt', $gw_about_id ) ) : ?>
				<p class="lede"><?php echo esc_html( get_post_field( 'post_excerpt', $gw_about_id ) ); ?></p>
			<?php else : ?>
				<p class="lede">Lauren Goodwin is a decorative painter based in Mayfield East. Her career began in New York, applying design work across film, retail and interiors. In 2018 she founded Lauren Goodwin Decorative Finishes, bringing together art, architecture and the textures she grew up around.</p>
			<?php endif; ?>

			<ul class="creds">
				<li><span>Specialist in</span><span>Microcement, Venetian plaster, Marmorino</span></li>
				<li><span>Trained in</span><span>New York City</span></li>
				<li><span>Based in</span><span><?php echo esc_html( gw_contact( 'address' ) ); ?></span></li>
				<li><span>Working across</span><span>Newcastle · Port Stephens · Central Coast</span></li>
				<li><span>Works with</span><span>Builders · Interior designers · Homeowners</span></li>
			</ul>

			<a class="btn" href="#contact">Talk to Lauren</a>
		</div>
	</div>
</section>
