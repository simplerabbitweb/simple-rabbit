<?php
/**
 * Document head and site header.
 *
 * @package goodwin
 */

?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	<?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<a class="skip-link screen-reader-text" href="#main">Skip to content</a>

<header class="topbar" id="topbar">
	<a class="mark" href="<?php echo esc_url( home_url( '/' ) ); ?>">
		<?php gw_logo(); ?>
		<span class="screen-reader-text"><?php bloginfo( 'name' ); ?></span>
	</a>

	<button class="navtoggle" id="navtoggle" aria-expanded="false" aria-controls="nav">Menu</button>

	<nav class="nav" id="nav" aria-label="Primary">
		<?php
		if ( has_nav_menu( 'primary' ) ) {
			wp_nav_menu(
				array(
					'theme_location' => 'primary',
					'container'      => false,
					'items_wrap'     => '<ul class="navlist">%3$s</ul>',
					'depth'          => 1,
				)
			);
		} else {
			// Sensible default until a menu is assigned in Appearance → Menus.
			?>
			<ul class="navlist">
			<li><a href="<?php echo esc_url( home_url( '/#work' ) ); ?>">Projects</a></li>
			<li><a href="<?php echo esc_url( home_url( '/#finishes' ) ); ?>">Finishes</a></li>
			<li><a href="<?php echo esc_url( home_url( '/#about' ) ); ?>">About</a></li>
			<li><a href="<?php echo esc_url( home_url( '/#contact' ) ); ?>">Contact</a></li>
			</ul>
			<?php
		}
		?>
		<a class="tel" href="tel:<?php echo esc_attr( gw_contact( 'phone_link' ) ); ?>">
			<?php echo esc_html( gw_contact( 'phone' ) ); ?>
		</a>
	</nav>
</header>

<main id="main">
