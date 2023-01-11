DO $$ DECLARE 
	weeks_in_top10 top10_by_contries.cumulative_weeks_in_top_10%TYPE;
	BEGIN weeks_in_top10 := 10;
	FOR counter IN 1..5 LOOP
	INSERT INTO
	    top10_by_contries(
	        country_iso2,
	        show_id,
	        week,
	        weekly_rank,
	        cumulative_weeks_in_top_10
	    )
	VALUES (
	        'UA',
	        counter,
	        current_date - counter + 1,
	        counter + 1,
	        weeks_in_top10 - counter
	    );
	END LOOP;
	END;
	$$ 
