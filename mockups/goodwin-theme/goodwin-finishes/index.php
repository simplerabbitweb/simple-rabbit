<?php
/**
 * Fallback template — blog listing and anything without a more specific file.
 *
 * @package goodwin
 */

get_header();
?>

<section class="page-body wrap">
	<p class="label"><?php bloginfo( 'name' ); ?></p>
	<h1 style="font-size:clamp(2.5rem,5vw,4rem)">
		<?php
		if ( is_search() ) {
			printf( 'Search: %s', esc_html( get_search_query() ) );
		} elseif ( is_archive() ) {
			the_archive_title();
		} else {
			echo 'Journal';
		}
		?>
	</h1>

	<?php if ( have_posts() ) : ?>
		<div class="creds" style="max-width:none;margin-top:2.5rem">
			<?php
			while ( have_posts() ) :
				the_post();
				?>
				<li style="align-items:baseline">
					<span><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></span>
					<span><?php echo esc_html( get_the_date() ); ?></span>
				</li>
				<?php
			endwhile;
			?>
		</div>

		<div style="margin-top:2.5rem"><?php the_posts_pagination(); ?></div>
	<?php else : ?>
		<p class="notice">Nothing here yet.</p>
	<?php endif; ?>
</section>

<?php
get_footer();
