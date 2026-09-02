<?php
/**
 * Plugin Name: Goodwin Project Importer (one-time)
 * Description: Creates Project posts from images already in the Media Library, matching on filename. Dry run first. Delete this plugin once the import is done.
 * Version: 1.0.0
 * Author: Simple Rabbit
 * Requires PHP: 8.0
 *
 * Usage: Tools → Import Goodwin projects. Preview the match table, then import.
 * WP-CLI: wp goodwin import --dry-run   /   wp goodwin import   /   wp goodwin rollback
 *
 * @package goodwin
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/* ═══════════════════════════════════════════════════════════════════════
   THE BATCH
   One row per project. To import a second batch later, replace this array
   and run the plugin again — anything already imported is skipped.

   file     Original filename from the staging site. Matching ignores WordPress
            suffixes (-scaled, -e1733666879220, -400x284, -1), so IMG_6530.jpg
            and IMG_6530-scaled-e1733666879220.jpg both find the same image.
   cat      Finish term slug: microcement | venetian | limewash | faux | commercial
   featured Show in the homepage gallery.
   ═══════════════════════════════════════════════════════════════════════ */

function gw_import_batch() {
	return array(
		array( 'file' => 'IMG_6530-scaled-e1733666879220.jpg', 'title' => 'Arched niche, ensuite', 'cat' => 'venetian', 'finish' => 'Marmorino, burnished', 'loc' => 'Merewether', 'space' => 'Ensuite', 'featured' => true, 'desc' => "A curved niche cut into the wall and plastered in three coats, so the arch reads as one continuous surface when the afternoon light rakes across it." ),
		array( 'file' => 'IMG_7984.jpg', 'title' => 'Fireplace surround', 'cat' => 'venetian', 'finish' => 'Venetian plaster', 'loc' => 'Bar Beach', 'space' => 'Living room', 'featured' => true, 'desc' => "A warm off-white plaster wrapped around the firebox, tinted half a shade deeper than the walls either side." ),
		array( 'file' => 'IMG_3137.jpg', 'title' => 'Curved ensuite', 'cat' => 'microcement', 'finish' => 'Microcement, sealed', 'loc' => 'Warners Bay', 'space' => 'Ensuite', 'featured' => true, 'desc' => "Walls, curved shower return and floor in a single microcement system — no grout lines anywhere in the room." ),
		array( 'file' => 'IMG_0731.jpg', 'title' => 'Walk-in shower', 'cat' => 'microcement', 'finish' => 'Microcement, matte seal', 'loc' => 'Newcastle East', 'space' => 'Bathroom', 'featured' => false, 'desc' => "Brass tapware set against a soft white microcement wall, with a recessed shelf formed before the finish coat." ),
		array( 'file' => 'IMG_0719.jpg', 'title' => 'Guest bathroom', 'cat' => 'venetian', 'finish' => 'Polished plaster', 'loc' => 'Port Stephens', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A warm sand-toned plaster that picks up the timber louvre door and the bushland outside the window." ),
		array( 'file' => 'IMG_0746.jpg', 'title' => 'Bath alcove', 'cat' => 'venetian', 'finish' => 'Venetian plaster', 'loc' => 'Hamilton', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A quiet alcove finished corner to corner, with the arched niche formed and plastered in the same pass." ),
		array( 'file' => 'IMG_3154.jpg', 'title' => 'Wet room', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Merewether', 'space' => 'Wet room', 'featured' => true, 'desc' => "Ceiling, walls and floor in one tone so the shower reads as a single carved volume." ),
		array( 'file' => 'IMG_3215.jpg', 'title' => 'Family bathroom', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Medowie', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A curved shower wall built and finished on site, sitting above a tiled floor from the original build." ),
		array( 'file' => 'IMG_3175.jpg', 'title' => 'Vanity wall', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Cooks Hill', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A soft, cloud-free finish behind a stone basin, kept deliberately flat so the tapware does the talking." ),
		array( 'file' => 'IMG_3135-scaled.jpg', 'title' => 'Full wet area', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Newcastle', 'space' => 'Ensuite', 'featured' => false, 'desc' => "Every surface except the ceiling, including the vanity and a wrapped cupboard." ),
		array( 'file' => 'IMG_4844.jpg', 'title' => 'Entry column', 'cat' => 'limewash', 'finish' => 'Lime wash', 'loc' => 'Stockton', 'space' => 'Entry', 'featured' => false, 'desc' => "Lime wash over a rendered column and adjoining wall, laid on in soft cross-strokes for movement." ),
		array( 'file' => 'IMG_7445.jpg', 'title' => 'Vaulted booths', 'cat' => 'commercial', 'finish' => 'Marmorino, tinted', 'loc' => 'Newcastle West', 'space' => 'Hospitality', 'featured' => true, 'desc' => "Arched booth vaults finished in a pale blue Marmorino, with LED strips set into the reveal." ),
		array( 'file' => 'IMG_7585.jpg', 'title' => 'Shower surround', 'cat' => 'venetian', 'finish' => 'Venetian plaster', 'loc' => 'New Lambton', 'space' => 'Bathroom', 'featured' => false, 'desc' => "Plaster taken to the glass line where it meets travertine tile, sealed for daily wet-area use." ),
		array( 'file' => 'IMG_8440.jpg', 'title' => "Butler's pantry", 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Fern Bay', 'space' => 'Kitchen', 'featured' => false, 'desc' => "Walls and open shelving niches finished together so the joinery disappears into the wall." ),
		array( 'file' => 'IMG_8487.jpg', 'title' => 'Powder room', 'cat' => 'limewash', 'finish' => 'Lime wash', 'loc' => 'Medowie', 'space' => 'Powder room', 'featured' => true, 'desc' => "A warm, mottled lime wash that shifts through the day with the light off the paddocks." ),
		array( 'file' => 'IMG_8489.jpg', 'title' => 'Bench and window reveal', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Medowie', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A built-in bench wrapped in microcement, carried up the wall and around the window reveal." ),
		array( 'file' => 'IMG_8500.jpg', 'title' => 'Niche and bench', 'cat' => 'venetian', 'finish' => 'Marmorino', 'loc' => 'Medowie', 'space' => 'Bathroom', 'featured' => false, 'desc' => "A square niche and seat finished in a cream Marmorino above a terracotta tiled floor." ),
		array( 'file' => 'IMG_8553.jpg', 'title' => 'Kitchen splashback', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Adamstown', 'space' => 'Kitchen', 'featured' => false, 'desc' => "A grout-free splashback taken up behind the timber shelf and returned into the reveal." ),
		array( 'file' => 'IMG_8570.jpg', 'title' => 'Reception counter', 'cat' => 'commercial', 'finish' => 'Marmorino', 'loc' => 'Newcastle CBD', 'space' => 'Commercial', 'featured' => false, 'desc' => "A curved reception counter finished on site, with a timber kick and cap left exposed." ),
		array( 'file' => 'IMG_8722-scaled.jpg', 'title' => 'Shower niches', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Charlestown', 'space' => 'Bathroom', 'featured' => false, 'desc' => "Three stacked niches formed in the wall and finished seamlessly with the surrounding surface." ),
		array( 'file' => 'IMG_8747-scaled.jpg', 'title' => 'Half-moon wall lights', 'cat' => 'venetian', 'finish' => 'Venetian plaster', 'loc' => 'Bar Beach', 'space' => 'Hallway', 'featured' => true, 'desc' => "Plaster burnished to a low sheen so the wall lights wash across it without hot spots." ),
		array( 'file' => 'IMG_8741-scaled.jpg', 'title' => 'Lit entry niches', 'cat' => 'venetian', 'finish' => 'Marmorino', 'loc' => 'Merewether', 'space' => 'Entry', 'featured' => false, 'desc' => "Three lit niches set into a plastered entry wall beside a solid timber door." ),
		array( 'file' => 'IMG_2723-1.jpeg', 'title' => 'Wet area and mosaic', 'cat' => 'microcement', 'finish' => 'Microcement', 'loc' => 'Mayfield', 'space' => 'Bathroom', 'featured' => false, 'desc' => "Microcement walls meeting a pebble mosaic band, with black tapware set through the finish." ),
		array( 'file' => 'IMG_3472.jpg', 'title' => 'Backlit porthole hallway', 'cat' => 'faux', 'finish' => 'Textured render, hand-worked', 'loc' => 'Newcastle', 'space' => 'Hallway', 'featured' => true, 'desc' => "A deep grey textured wall worked around a backlit porthole, so the light throws its own texture." ),
		array( 'file' => 'IMG_3648.jpg', 'title' => 'Pink feature wall', 'cat' => 'limewash', 'finish' => 'Lime wash, custom tint', 'loc' => 'Hamilton', 'space' => 'Feature wall', 'featured' => true, 'desc' => "A custom rose tint laid in soft cloudy passes — three samples on site before the colour was locked." ),
		array( 'file' => 'IMG_6896.jpg', 'title' => 'Bar arches', 'cat' => 'commercial', 'finish' => 'Marmorino, tinted', 'loc' => 'Newcastle CBD', 'space' => 'Hospitality', 'featured' => true, 'desc' => "Back-bar arches finished in a deep blue-grey to sit behind glassware and warm lighting." ),
		array( 'file' => 'IMG_6879.jpg', 'title' => 'Aged timber effect', 'cat' => 'faux', 'finish' => 'Faux timber', 'loc' => 'Stockton', 'space' => 'Feature wall', 'featured' => false, 'desc' => "A weathered timber effect painted by hand over a corrugated profile, grain and all." ),
		array( 'file' => 'IMG_2938.jpg', 'title' => 'Metallic ceiling feature', 'cat' => 'faux', 'finish' => 'Metallic leaf', 'loc' => 'Newcastle CBD', 'space' => 'Commercial', 'featured' => false, 'desc' => "A burnished metallic panel set into the ceiling, lit from a concealed cove around the edge." ),
		array( 'file' => 'IMG_2737.jpg', 'title' => 'Stone-effect corridor', 'cat' => 'commercial', 'finish' => 'Faux stone', 'loc' => 'Sydney', 'space' => 'Commercial', 'featured' => false, 'desc' => "Curved corridor walls painted to read as book-matched stone, matched to a sample supplied by the architect." ),
		array( 'file' => 'IMG_6711.jpg', 'title' => 'Concrete-look ceiling', 'cat' => 'microcement', 'finish' => 'Microcement, ceiling', 'loc' => 'Port Stephens', 'space' => 'Living room', 'featured' => false, 'desc' => "A concrete-look ceiling applied overhead in thin coats, with rattan pendants dropped through." ),
	);
}

/* ═════════════════════════  MATCHING  ═════════════════════════ */

/**
 * Reduce a filename to a comparable stem.
 *
 * WordPress appends its own suffixes: -scaled for large uploads, -e1733666879220
 * for edited images, -400x284 for generated sizes, -1 for duplicate names. All of
 * them are stripped so IMG_6530-scaled-e1733666879220.jpg and IMG_6530.jpg match.
 *
 * @param string $filename Any filename.
 * @return string Lowercase stem.
 */
function gw_import_stem( $filename ) {
	$stem = pathinfo( $filename, PATHINFO_FILENAME );
	$stem = preg_replace( '/-e\d{10,}$/', '', $stem );   // edited copy
	$stem = preg_replace( '/-scaled$/', '', $stem );      // scaled original
	$stem = preg_replace( '/-\d+x\d+$/', '', $stem );     // generated size
	$stem = preg_replace( '/-\d{1,2}$/', '', $stem );     // duplicate suffix
	$stem = preg_replace( '/-scaled$/', '', $stem );      // -scaled behind an -e suffix

	return strtolower( $stem );
}

/**
 * Build a stem => attachment ID map of the whole media library, once.
 *
 * @return array
 */
function gw_import_media_map() {
	static $map = null;

	if ( null !== $map ) {
		return $map;
	}

	$map = array();

	$attachments = get_posts(
		array(
			'post_type'      => 'attachment',
			'post_mime_type' => 'image',
			'posts_per_page' => -1,
			'post_status'    => 'inherit',
			'fields'         => 'ids',
		)
	);

	foreach ( $attachments as $id ) {
		$file = get_post_meta( $id, '_wp_attached_file', true );

		if ( ! $file ) {
			continue;
		}

		$stem = gw_import_stem( basename( $file ) );

		// Keep the earliest (lowest ID) match — that's the original upload.
		if ( ! isset( $map[ $stem ] ) || $id < $map[ $stem ] ) {
			$map[ $stem ] = (int) $id;
		}
	}

	return $map;
}

/**
 * Work out what the import would do, without doing it.
 *
 * @return array Rows with keys: row, attachment_id, existing_id, status.
 */
function gw_import_plan() {
	$map  = gw_import_media_map();
	$plan = array();

	foreach ( gw_import_batch() as $row ) {
		$stem       = gw_import_stem( $row['file'] );
		$attachment = isset( $map[ $stem ] ) ? $map[ $stem ] : 0;

		$existing = get_posts(
			array(
				'post_type'      => 'project',
				'post_status'    => 'any',
				'posts_per_page' => 1,
				'fields'         => 'ids',
				'meta_key'       => '_gw_import_key',
				'meta_value'     => $stem,
			)
		);

		if ( $existing ) {
			$status = 'already imported';
		} elseif ( ! $attachment ) {
			$status = 'image not found';
		} else {
			$status = 'ready';
		}

		$plan[] = array(
			'row'           => $row,
			'stem'          => $stem,
			'attachment_id' => $attachment,
			'existing_id'   => $existing ? (int) $existing[0] : 0,
			'status'        => $status,
		);
	}

	return $plan;
}

/* ═════════════════════════  IMPORT  ═════════════════════════ */

/**
 * Create the projects.
 *
 * @return array Counts: created, skipped, missing.
 */
function gw_import_run() {
	$counts = array( 'created' => 0, 'skipped' => 0, 'missing' => 0 );
	$order  = 0;

	foreach ( gw_import_plan() as $item ) {
		$order++;

		if ( 'ready' !== $item['status'] ) {
			$counts[ 'image not found' === $item['status'] ? 'missing' : 'skipped' ]++;
			continue;
		}

		$row = $item['row'];

		$post_id = wp_insert_post(
			array(
				'post_type'    => 'project',
				'post_status'  => 'publish',
				'post_title'   => $row['title'],
				'post_content' => $row['desc'],
				'menu_order'   => $order,
			),
			true
		);

		if ( is_wp_error( $post_id ) ) {
			$counts['skipped']++;
			continue;
		}

		set_post_thumbnail( $post_id, $item['attachment_id'] );
		wp_set_object_terms( $post_id, $row['cat'], 'project_category' );

		// Marks the project as ours, for rollback and for skipping on re-run.
		update_post_meta( $post_id, '_gw_import_key', $item['stem'] );

		$fields = array(
			'field_gw_location' => $row['loc'],
			'field_gw_finish'   => $row['finish'],
			'field_gw_space'    => $row['space'],
			'field_gw_featured' => $row['featured'] ? 1 : 0,
		);

		foreach ( $fields as $key => $value ) {
			if ( function_exists( 'update_field' ) ) {
				update_field( $key, $value, $post_id );
			}
		}

		// Alt text, only where the image doesn't already have one.
		$alt = get_post_meta( $item['attachment_id'], '_wp_attachment_image_alt', true );

		if ( ! $alt ) {
			update_post_meta(
				$item['attachment_id'],
				'_wp_attachment_image_alt',
				sprintf( '%s in %s, %s', $row['title'], strtolower( $row['finish'] ), $row['loc'] )
			);
		}

		$counts['created']++;
	}

	return $counts;
}

/**
 * Bin everything this importer created.
 *
 * @return int Number trashed.
 */
function gw_import_rollback() {
	$ids = get_posts(
		array(
			'post_type'      => 'project',
			'post_status'    => 'any',
			'posts_per_page' => -1,
			'fields'         => 'ids',
			'meta_key'       => '_gw_import_key',
		)
	);

	foreach ( $ids as $id ) {
		wp_trash_post( $id );
	}

	return count( $ids );
}

/* ═════════════════════════  ADMIN SCREEN  ═════════════════════════ */

/**
 * Add the Tools page.
 */
function gw_import_menu() {
	add_management_page(
		'Import Goodwin projects',
		'Import Goodwin projects',
		'manage_options',
		'gw-import',
		'gw_import_screen'
	);
}
add_action( 'admin_menu', 'gw_import_menu' );

/**
 * The Tools → Import screen.
 */
function gw_import_screen() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( 'Not allowed.' );
	}

	$notice = '';

	if ( isset( $_POST['gw_action'] ) ) {
		check_admin_referer( 'gw_import' );

		if ( 'import' === $_POST['gw_action'] ) {
			$counts = gw_import_run();
			$notice = sprintf(
				'Imported %d project(s). Skipped %d already imported. %d image(s) not found.',
				$counts['created'],
				$counts['skipped'],
				$counts['missing']
			);
		}

		if ( 'rollback' === $_POST['gw_action'] ) {
			$notice = sprintf( 'Moved %d imported project(s) to the bin.', gw_import_rollback() );
		}
	}

	$plan    = gw_import_plan();
	$ready   = count( array_filter( $plan, fn( $i ) => 'ready' === $i['status'] ) );
	$missing = count( array_filter( $plan, fn( $i ) => 'image not found' === $i['status'] ) );
	?>
	<div class="wrap">
		<h1>Import Goodwin projects</h1>

		<?php if ( $notice ) : ?>
			<div class="notice notice-success"><p><?php echo esc_html( $notice ); ?></p></div>
		<?php endif; ?>

		<?php if ( ! function_exists( 'update_field' ) ) : ?>
			<div class="notice notice-warning"><p>ACF is not active. Projects will be created with images and finishes, but location, finish and space will be empty.</p></div>
		<?php endif; ?>

		<p>
			<strong><?php echo esc_html( $ready ); ?></strong> ready to import,
			<strong><?php echo esc_html( $missing ); ?></strong> with no matching image in the Media Library.
			Nothing is created until you press Import.
		</p>

		<form method="post">
			<?php wp_nonce_field( 'gw_import' ); ?>
			<p>
				<button class="button button-primary" name="gw_action" value="import" <?php disabled( 0, $ready ); ?>>
					Import <?php echo esc_html( $ready ); ?> project(s)
				</button>
				<button class="button" name="gw_action" value="rollback"
					onclick="return confirm('Move every imported project to the bin?')">
					Undo import
				</button>
			</p>
		</form>

		<table class="widefat striped">
			<thead>
				<tr>
					<th style="width:70px">Image</th>
					<th>Project</th>
					<th>Finish</th>
					<th>Location</th>
					<th>Source file</th>
					<th>Status</th>
				</tr>
			</thead>
			<tbody>
				<?php foreach ( $plan as $item ) : ?>
					<tr>
						<td>
							<?php
							if ( $item['attachment_id'] ) {
								echo wp_get_attachment_image( $item['attachment_id'], array( 60, 60 ), true, array( 'style' => 'object-fit:cover;width:60px;height:60px' ) );
							}
							?>
						</td>
						<td><strong><?php echo esc_html( $item['row']['title'] ); ?></strong><?php echo $item['row']['featured'] ? ' ★' : ''; ?></td>
						<td><?php echo esc_html( $item['row']['finish'] ); ?></td>
						<td><?php echo esc_html( $item['row']['loc'] ); ?></td>
						<td><code><?php echo esc_html( $item['row']['file'] ); ?></code></td>
						<td>
							<?php if ( 'ready' === $item['status'] ) : ?>
								<span style="color:#008a20">Ready</span>
							<?php elseif ( 'already imported' === $item['status'] ) : ?>
								<a href="<?php echo esc_url( get_edit_post_link( $item['existing_id'] ) ); ?>">Already imported</a>
							<?php else : ?>
								<span style="color:#b32d2e">Image not found</span>
							<?php endif; ?>
						</td>
					</tr>
				<?php endforeach; ?>
			</tbody>
		</table>

		<p class="description" style="margin-top:1rem">
			Titles, locations and descriptions are placeholders written for the design mockup.
			Check them against Lauren's records before this site goes live.
		</p>
	</div>
	<?php
}

/* ═════════════════════════  WP-CLI  ═════════════════════════ */

if ( defined( 'WP_CLI' ) && WP_CLI ) {
	WP_CLI::add_command(
		'goodwin import',
		function ( $args, $assoc ) {
			if ( isset( $assoc['dry-run'] ) ) {
				$rows = array();

				foreach ( gw_import_plan() as $item ) {
					$rows[] = array(
						'title'  => $item['row']['title'],
						'file'   => $item['row']['file'],
						'image'  => $item['attachment_id'] ? $item['attachment_id'] : '—',
						'status' => $item['status'],
					);
				}

				WP_CLI\Utils\format_items( 'table', $rows, array( 'title', 'file', 'image', 'status' ) );
				return;
			}

			$counts = gw_import_run();
			WP_CLI::success( sprintf( 'Created %d, skipped %d, missing %d.', $counts['created'], $counts['skipped'], $counts['missing'] ) );
		}
	);

	WP_CLI::add_command(
		'goodwin rollback',
		function () {
			WP_CLI::success( sprintf( 'Binned %d project(s).', gw_import_rollback() ) );
		}
	);
}
