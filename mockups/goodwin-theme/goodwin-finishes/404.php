<?php
/**
 * 404.
 *
 * @package goodwin
 */

get_header();
?>

<section class="page-body wrap">
	<p class="label">Page not found</p>
	<h1 style="font-size:clamp(2.5rem,5vw,4rem)">That page has been <em style="font-style:italic;color:var(--accent)">plastered over</em></h1>
	<p class="lede" style="margin-top:1.2rem">The link may be old, or the page may have moved. The work is all still here.</p>
	<p style="margin-top:2rem">
		<a class="btn btn--solid" href="<?php echo esc_url( home_url( '/#work' ) ); ?>">View projects</a>
	</p>
</section>

<?php
get_footer();
