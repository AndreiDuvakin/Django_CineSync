CREATE OR REPLACE FUNCTION populate_film_sessions(start_date_session date)
RETURNS VOID AS $$
DECLARE
    film_count INT := 26;  -- Общее количество фильмов
    auditorium_count INT := 7;  -- Общее количество залов
    days_to_populate INT := 5;  -- Количество дней для заполнения
    start_date DATE := start_date_session + INTERVAL '1 day';  -- Начальная дата заполнения (завтра)
    session_times TIME[] := ARRAY['10:00'::TIME, '13:30'::TIME, '17:00'::TIME, '20:30'::TIME];  -- Время сеансов
    film_id INT;
    start_datetime TIMESTAMP;
    end_datetime TIMESTAMP;
BEGIN
    FOR i IN 0..(days_to_populate - 1) LOOP
        FOR j IN 1..auditorium_count LOOP
            FOR k IN 1..4 LOOP
                -- Выбор случайного фильма
                PERFORM setseed(random());
                film_id := (SELECT id FROM films_films ORDER BY random() LIMIT 1);

                -- Вычисление даты и времени начала сеанса
                start_datetime := COALESCE(start_date + i + session_times[k], start_date);
                end_datetime := COALESCE(start_datetime + INTERVAL '2 hours', start_datetime);  -- Длительность фильма 2 часа

                -- Вставка данных в таблицу
                INSERT INTO timetable_film_sessions (start_datetime, end_datetime, price, film_id, auditorium_id)
                VALUES (start_datetime, end_datetime, round(random() * 500 + 200), film_id, j);
            END LOOP;
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
