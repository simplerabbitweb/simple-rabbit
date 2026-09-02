<?php
/**
 * Goodwin Decorative Finishes — theme setup.
 *
 * @package goodwin
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

define( 'GW_VERSION', '1.1.0' );

require_once get_template_directory() . '/inc/cpt.php';
require_once get_template_directory() . '/inc/acf-fields.php';
require_once get_template_directory() . '/inc/template-tags.php';

/**
 * Theme supports, menus, image sizes.
 */
function gw_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'automatic-feed-links' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption', 'style', 'script' ) );

	register_nav_menus(
		array(
			'primary' => __( 'Primary menu', 'goodwin' ),
		)
	);

	// Lets the logo be swapped in the Customizer; the bundled SVG is the default.
	add_theme_support(
		'custom-logo',
		array(
			'height'      => 131,
			'width'       => 375,
			'flex-height' => true,
			'flex-width'  => true,
		)
	);

	// Grid tiles are portrait; the lightbox and hero want the long edge.
	add_image_size( 'gw-grid', 800, 1067, true );
	add_image_size( 'gw-square', 800, 800, true );
	add_image_size( 'gw-full', 1800, 1800, false );
}
add_action( 'after_setup_theme', 'gw_setup' );

/**
 * Styles and scripts.
 */
function gw_assets() {
	wp_enqueue_style(
		'gw-fonts',
		'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap',
		array(),
		null
	);

	wp_enqueue_style(
		'gw-style',
		get_stylesheet_uri(),
		array( 'gw-fonts' ),
		filemtime( get_template_directory() . '/style.css' )
	);

	wp_enqueue_script(
		'gw-gallery',
		get_template_directory_uri() . '/assets/js/gallery.js',
		array(),
		filemtime( get_template_directory() . '/assets/js/gallery.js' ),
		true
	);
}
add_action( 'wp_enqueue_scripts', 'gw_assets' );

/**
 * Preconnect to the font host so the display face lands sooner.
 */
function gw_resource_hints( $urls, $relation ) {
	if ( 'preconnect' === $relation ) {
		$urls[] = array( 'href' => 'https://fonts.gstatic.com', 'crossorigin' );
	}
	return $urls;
}
add_filter( 'wp_resource_hints', 'gw_resource_hints', 10, 2 );

/**
 * Site-wide contact details, edited in Settings → Contact details.
 *
 * Kept in options rather than hardcoded so Lauren can change a phone number
 * without touching a template.
 *
 * @param string $key One of phone, phone_link, email, address, instagram, licence.
 * @return string
 */
function gw_contact( $key ) {
	$defaults = array(
		'phone'      => '+61 488 330 997',
		'phone_link' => '+61488330997',
		'email'      => 'hello@goodwinfinishes.com.au',
		'address'    => 'Mayfield East, Newcastle NSW 2304',
		'instagram'  => 'laurengoodwin_decorativefinish',
		'licence'    => '#456042C',
		'form_endpoint' => 'https://formspree.io/f/mqpzjnyl',
	);

	$value = get_option( 'gw_' . $key, '' );

	return $value ? $value : ( isset( $defaults[ $key ] ) ? $defaults[ $key ] : '' );
}

/**
 * Register the contact detail fields on Settings → General.
 */
function gw_register_settings() {
	$fields = array(
		'gw_phone'      => 'Phone (display)',
		'gw_phone_link' => 'Phone (dial format, e.g. +61488330997)',
		'gw_email'      => 'Email',
		'gw_address'    => 'Studio location',
		'gw_instagram'  => 'Instagram handle (no @)',
		'gw_licence'    => 'Licence number',
		'gw_form_endpoint' => 'Enquiry form endpoint (Formspree)',
	);

	add_settings_section( 'gw_contact_section', 'Goodwin contact details', '__return_false', 'general' );

	foreach ( $fields as $key => $label ) {
		register_setting( 'general', $key, array( 'sanitize_callback' => 'sanitize_text_field' ) );

		add_settings_field(
			$key,
			esc_html( $label ),
			function () use ( $key ) {
				printf(
					'<input type="text" id="%1$s" name="%1$s" value="%2$s" class="regular-text">',
					esc_attr( $key ),
					esc_attr( get_option( $key, '' ) )
				);
			},
			'general',
			'gw_contact_section',
			array( 'label_for' => $key )
		);
	}
}
add_action( 'admin_init', 'gw_register_settings' );

/**
 * Flush rewrite rules on activation, and again whenever this theme's rewrite
 * version changes — updating a theme in place does not fire after_switch_theme,
 * so old project URLs would otherwise linger.
 */
function gw_flush_rewrites() {
	gw_register_project_cpt();
	flush_rewrite_rules();
	update_option( 'gw_rewrite_version', GW_VERSION );
}
add_action( 'after_switch_theme', 'gw_flush_rewrites' );

/**
 * Catch in-place theme updates.
 */
function gw_maybe_flush() {
	if ( get_option( 'gw_rewrite_version' ) !== GW_VERSION ) {
		gw_flush_rewrites();
	}
}
add_action( 'admin_init', 'gw_maybe_flush' );

/**
 * Tell the admin what the theme still needs.
 */
function gw_admin_notices() {
	if ( ! current_user_can( 'manage_options' ) ) {
		return;
	}

	if ( ! function_exists( 'get_field' ) ) {
		echo '<div class="notice notice-warning"><p><strong>Goodwin theme:</strong> Advanced Custom Fields Pro is not active. Project pages will show titles and featured images only — the gallery, location and finish fields need ACF Pro.</p></div>';
	}
}
add_action( 'admin_notices', 'gw_admin_notices' );
