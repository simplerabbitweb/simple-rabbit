<?php
/**
 * ACF field group for Projects, registered in code so it lives in version
 * control rather than only in the database.
 *
 * The gallery field requires ACF Pro. Everything else works on ACF free.
 *
 * @package goodwin
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Register the Project details field group.
 */
function gw_register_fields() {
	if ( ! function_exists( 'acf_add_local_field_group' ) ) {
		return;
	}

	acf_add_local_field_group(
		array(
			'key'                   => 'group_gw_project',
			'title'                 => 'Project details',
			'location'              => array(
				array(
					array(
						'param'    => 'post_type',
						'operator' => '==',
						'value'    => 'project',
					),
				),
			),
			'menu_order'            => 0,
			'position'              => 'normal',
			'style'                 => 'default',
			'label_placement'       => 'top',
			'hide_on_screen'        => array( 'discussion', 'comments', 'trackbacks', 'custom_fields' ),
			'fields'                => array(
				array(
					'key'          => 'field_gw_gallery',
					'label'        => 'Photos',
					'name'         => 'gallery',
					'type'         => 'gallery',
					'instructions' => 'Drag photos in, drag to reorder. The main image at the top right is the one that shows in the grid.',
					'preview_size' => 'medium',
					'insert'       => 'append',
					'library'      => 'all',
				),
				array(
					'key'          => 'field_gw_location',
					'label'        => 'Location',
					'name'         => 'location',
					'type'         => 'text',
					'instructions' => 'Suburb, e.g. Merewether. Shows under the project title and helps local search.',
					'wrapper'      => array( 'width' => '33' ),
				),
				array(
					'key'          => 'field_gw_finish',
					'label'        => 'Finish used',
					'name'         => 'finish',
					'type'         => 'text',
					'instructions' => 'e.g. Microcement, sealed.',
					'wrapper'      => array( 'width' => '33' ),
				),
				array(
					'key'          => 'field_gw_space',
					'label'        => 'Space',
					'name'         => 'space',
					'type'         => 'text',
					'instructions' => 'e.g. Ensuite, kitchen, hallway.',
					'wrapper'      => array( 'width' => '34' ),
				),
				array(
					'key'     => 'field_gw_client_type',
					'label'   => 'Client type',
					'name'    => 'client_type',
					'type'    => 'select',
					'choices' => array(
						''          => '—',
						'homeowner' => 'Homeowner',
						'builder'   => 'Builder',
						'designer'  => 'Interior designer',
						'commercial'=> 'Commercial',
					),
					'wrapper' => array( 'width' => '50' ),
				),
				array(
					'key'          => 'field_gw_featured',
					'label'        => 'Show on homepage',
					'name'         => 'featured',
					'type'         => 'true_false',
					'instructions' => 'Featured projects fill the homepage gallery.',
					'ui'           => 1,
					'wrapper'      => array( 'width' => '50' ),
				),
				array(
					'key'          => 'field_gw_before',
					'label'        => 'Before photo',
					'name'         => 'before_image',
					'type'         => 'image',
					'instructions' => 'Optional. Shown beside the after photo.',
					'return_format'=> 'array',
					'preview_size' => 'medium',
					'wrapper'      => array( 'width' => '50' ),
				),
				array(
					'key'          => 'field_gw_after',
					'label'        => 'After photo',
					'name'         => 'after_image',
					'type'         => 'image',
					'return_format'=> 'array',
					'preview_size' => 'medium',
					'wrapper'      => array( 'width' => '50' ),
				),
			),
		)
	);
}
add_action( 'acf/init', 'gw_register_fields' );
