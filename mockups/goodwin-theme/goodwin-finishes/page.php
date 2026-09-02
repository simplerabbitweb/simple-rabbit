<?php
/**
 * Standard page.
 *
 * @package goodwin
 */

get_header();

while ( have_posts() ) :
	the_post();
	?>
	<article class="page-body wrap">
		<p class="label"><?php bloginfo( 'name' ); ?></p>
		<h1 style="font-size:clamp(2.5rem,5vw,4rem)"><?php the_title(); ?></h1>

		<?php if ( has_post_thumbnail() ) : ?>
			<figure class="project__hero"><?php the_post_thumbnail( 'gw-full' ); ?></figure>
		<?php endif; ?>

		<div class="entry-content" style="margin-top:2rem">
			<?php
			the_content();
			wp_link_pages();
			?>
		</div>
	</article>
	<?php
endwhile;

get_footer();
