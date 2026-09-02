<?php
/**
 * Instagram strip, contact block, colophon.
 *
 * @package goodwin
 */

$gw_instagram = gw_contact( 'instagram' );
?>

	<?php if ( $gw_instagram ) : ?>
		<section class="ig wrap">
			<div class="ig__head reveal">
				<div>
					<p class="label">Follow the work</p>
					<h2>@<?php echo esc_html( $gw_instagram ); ?></h2>
				</div>
				<a class="btn" href="https://www.instagram.com/<?php echo esc_attr( $gw_instagram ); ?>/" target="_blank" rel="noopener">Follow on Instagram</a>
			</div>

			<?php
			if ( shortcode_exists( 'instagram-feed' ) ) {
				// Smash Balloon, styled by the theme's .ig__strip rules.
				echo do_shortcode( '[instagram-feed num=6 cols=6 showheader=false showbutton=false showfollow=false]' );
			} else {
				// Fallback until the feed plugin is connected: recent project photos.
				$gw_recent = new WP_Query(
					array(
						'post_type'      => 'project',
						'posts_per_page' => 6,
						'meta_key'       => '_thumbnail_id',
					)
				);

				if ( $gw_recent->have_posts() ) :
					?>
					<div class="ig__strip">
						<?php
						while ( $gw_recent->have_posts() ) :
							$gw_recent->the_post();
							?>
							<a href="#work">
								<?php the_post_thumbnail( 'gw-square', array( 'loading' => 'lazy' ) ); ?>
							</a>
							<?php
						endwhile;
						?>
					</div>
					<?php
				endif;
				wp_reset_postdata();
			}
			?>
		</section>
	<?php endif; ?>

	<section class="contact" id="contact">
		<div class="wrap contact__grid">
			<div>
				<p class="label">Get in touch</p>
				<h2>Tell me about the <em>room</em></h2>
				<p class="lede" style="color:rgba(237,234,225,.78)">
					Send through the space, the finish you have in mind and a photo if you have one. Quotes are free.
				</p>

				<ul class="details">
					<li>
						<span>Phone</span>
						<span><a href="tel:<?php echo esc_attr( gw_contact( 'phone_link' ) ); ?>"><?php echo esc_html( gw_contact( 'phone' ) ); ?></a></span>
					</li>
					<li>
						<span>Email</span>
						<span><a href="mailto:<?php echo esc_attr( gw_contact( 'email' ) ); ?>"><?php echo esc_html( gw_contact( 'email' ) ); ?></a></span>
					</li>
					<li>
						<span>Studio</span>
						<span><?php echo esc_html( gw_contact( 'address' ) ); ?></span>
					</li>
					<?php if ( $gw_instagram ) : ?>
						<li>
							<span>Instagram</span>
							<span><a href="https://www.instagram.com/<?php echo esc_attr( $gw_instagram ); ?>/" target="_blank" rel="noopener">@<?php echo esc_html( $gw_instagram ); ?></a></span>
						</li>
					<?php endif; ?>
					<?php if ( gw_contact( 'licence' ) ) : ?>
						<li>
							<span>Licence</span>
							<span><?php echo esc_html( gw_contact( 'licence' ) ); ?></span>
						</li>
					<?php endif; ?>
				</ul>

				<?php if ( gw_svg( 'mineral-fix.svg' ) ) : ?>
					<div class="accred">
						<p class="label">Accredited applicator</p>
						<?php echo gw_svg( 'mineral-fix.svg' ); // phpcs:ignore WordPress.Security.EscapeOutput -- bundled theme asset. ?>
					</div>
				<?php endif; ?>
			</div>

			<form class="form" id="quoteform"
				action="<?php echo esc_url( gw_contact( 'form_endpoint' ) ); ?>"
				method="POST"
				data-email="<?php echo esc_attr( gw_contact( 'email' ) ); ?>">

				<input type="hidden" name="_subject" value="<?php echo esc_attr( 'New enquiry from ' . wp_parse_url( home_url(), PHP_URL_HOST ) ); ?>">

				<div class="field">
					<label for="f-name">Name</label>
					<input id="f-name" name="name" type="text" autocomplete="name" required>
				</div>
				<div class="field">
					<label for="f-email">Email</label>
					<input id="f-email" name="email" type="email" autocomplete="email" required>
				</div>
				<div class="field">
					<label for="f-phone">Phone</label>
					<input id="f-phone" name="phone" type="tel" autocomplete="tel">
				</div>
				<div class="field">
					<label for="f-address">Property address</label>
					<input id="f-address" name="address" type="text" autocomplete="street-address">
				</div>
				<div class="field">
					<label for="f-finish">Finish you're after</label>
					<select id="f-finish" name="finish">
						<option>Not sure yet</option>
						<?php
						$gw_finishes = get_terms(
							array(
								'taxonomy'   => 'project_category',
								'hide_empty' => false,
							)
						);

						if ( ! is_wp_error( $gw_finishes ) ) {
							foreach ( $gw_finishes as $gw_finish ) {
								echo '<option>' . esc_html( $gw_finish->name ) . '</option>';
							}
						}
						?>
					</select>
				</div>
				<div class="field">
					<label for="f-msg">About the space</label>
					<textarea id="f-msg" name="message" rows="3"></textarea>
				</div>

				<?php // Spam trap — hidden from people, tempting to bots. ?>
				<input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">

				<button class="btn btn--light" type="submit">Request a free quote</button>
				<p class="label" id="formstatus" role="status" aria-live="polite"></p>
			</form>
		</div>

		<div class="wrap colophon">
			<span>&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php bloginfo( 'name' ); ?></span>
			<span>Decorative wall finishes · Newcastle · Port Stephens · Central Coast</span>
			<span>Website designed and managed by <a href="https://simplerabbit.studio" target="_blank" rel="noopener">Simple Rabbit</a></span>
		</div>
	</section>
</main>

<?php wp_footer(); ?>
</body>
</html>
