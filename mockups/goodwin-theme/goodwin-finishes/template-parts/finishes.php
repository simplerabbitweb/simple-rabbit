<?php
/**
 * The four finish cards. Each links to its filtered project archive, and
 * borrows the newest project photo in that finish for its image.
 *
 * Edit the copy in $gw_cards. The slugs must match the Finish terms.
 *
 * @package goodwin
 */

$gw_cards = array(
	array(
		'slug'  => 'microcement',
		'title' => 'Microcement',
		'use'   => 'Wet areas · floors · joinery',
		'copy'  => 'A seamless, waterproof surface for bathrooms, floors and joinery. Modern, hard-wearing, and grout-free.',
	),
	array(
		'slug'  => 'venetian',
		'title' => 'Venetian Plaster<br>&amp; Marmorino',
		'use'   => 'Feature walls · fireplaces',
		'copy'  => 'Fine lime and marble dust, burnished in layers until the wall holds depth and light like stone.',
	),
	array(
		'slug'  => 'limewash',
		'title' => 'Lime Wash',
		'use'   => 'Whole rooms · ceilings',
		'copy'  => 'Soft, chalky movement across a whole room. Breathable, low-sheen, and endlessly tintable.',
	),
	array(
		'slug'  => 'faux',
		'title' => 'Decorative<br>&amp; Faux',
		'use'   => 'Bespoke effects · commercial',
		'copy'  => 'Aged timber, rusted steel, weathered stone, metallic leaf — effects painted by hand to order.',
	),
);
?>

<section class="finishes wrap" id="finishes">
	<div class="finishes__head reveal">
		<div>
			<p class="label">Finishes</p>
			<h2>A finish for every space</h2>
		</div>
		<a class="btn" href="#work">View projects by finish</a>
	</div>

	<div class="finishes__grid">
		<?php
		foreach ( $gw_cards as $gw_card ) :
			// Cards jump to the gallery and apply their filter — no separate page.
			$gw_link = '#work';
			$gw_img  = gw_term_image( $gw_card['slug'] );
			?>
			<article class="finish reveal">
				<div class="finish__img">
					<a href="<?php echo esc_url( $gw_link ); ?>" data-jump="<?php echo esc_attr( $gw_card['slug'] ); ?>">
						<?php
						if ( $gw_img ) {
							echo wp_get_attachment_image(
								$gw_img,
								'gw-grid',
								false,
								array(
									'loading' => 'lazy',
									'alt'     => esc_attr( wp_strip_all_tags( $gw_card['title'] ) . ' by Lauren Goodwin Decorative Finishes, Newcastle' ),
								)
							);
						}
						?>
					</a>
				</div>
				<p class="finish__use"><?php echo esc_html( $gw_card['use'] ); ?></p>
				<h3><?php echo wp_kses( $gw_card['title'], array( 'br' => array() ) ); ?></h3>
				<p><?php echo esc_html( $gw_card['copy'] ); ?></p>
				<a href="<?php echo esc_url( $gw_link ); ?>" data-jump="<?php echo esc_attr( $gw_card['slug'] ); ?>">See <?php echo esc_html( strtolower( wp_strip_all_tags( str_replace( '<br>', ' ', $gw_card['title'] ) ) ) ); ?> projects</a>
			</article>
		<?php endforeach; ?>
	</div>
</section>
