<?php
/**
 * Client quotes. Edit the array — three show at a time.
 *
 * Deliberately not a custom post type: they change once or twice a year, and
 * an extra admin menu for three quotes costs Lauren more than it saves.
 *
 * @package goodwin
 */

$gw_quotes = array(
	array(
		'quote' => 'Lauren is exceptional at her craft. She knows how to achieve your ideal finish to the highest of quality. My clients are blown away with how much her finishes have elevated their homes.',
		'name'  => 'Katrina H.',
		'role'  => 'Interior designer',
	),
	array(
		'quote' => 'Our bathroom involved micro-cementing everything except the ceiling. It was a big job but the quality was exceptional. She guided us through the whole process, even talking the other trades through it.',
		'name'  => 'Martha B.',
		'role'  => 'Full bathroom',
	),
	array(
		'quote' => 'I contacted her when another company did horrible quality work in my tattoo studio. Every client I have comments on how beautiful the paintwork is now.',
		'name'  => 'Ellie M.',
		'role'  => 'Tattoo studio',
	),
);
?>

<section class="words">
	<div class="wrap">
		<div class="reveal">
			<p class="label">In their words</p>
			<h2>What clients say afterwards</h2>
		</div>

		<div class="words__grid reveal">
			<?php foreach ( $gw_quotes as $gw_quote ) : ?>
				<blockquote class="quote">
					<p>&ldquo;<?php echo esc_html( $gw_quote['quote'] ); ?>&rdquo;</p>
					<footer>
						<?php echo esc_html( $gw_quote['name'] ); ?>
						<em><?php echo esc_html( $gw_quote['role'] ); ?></em>
					</footer>
				</blockquote>
			<?php endforeach; ?>
		</div>
	</div>
</section>
