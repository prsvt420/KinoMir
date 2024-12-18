run:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
dumpdata:
	poetry run python -Xutf8 manage.py dumpdata --indent=2 movies.Movie -o fixtures/movie.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 serials.Serial -o fixtures/serial.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 movies.FilmParticipant -o fixtures/film_participant.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 serials.SerialParticipant -o fixtures/serial_participant.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 core.Tag -o fixtures/tag.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 core.Genre -o fixtures/genre.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 core.Person -o fixtures/person.json
loaddata:
	poetry run python -Xutf8 manage.py loaddata fixtures/person.json
	poetry run python -Xutf8 manage.py loaddata fixtures/genre.json
	poetry run python -Xutf8 manage.py loaddata fixtures/tag.json
	poetry run python -Xutf8 manage.py loaddata fixtures/movie.json
	poetry run python -Xutf8 manage.py loaddata fixtures/serial.json
	poetry run python -Xutf8 manage.py loaddata fixtures/film_participant.json
	poetry run python -Xutf8 manage.py loaddata fixtures/serial_participant.json
tests:
	poetry run python manage.py test .
createsuperuser:
	poetry run python manage.py createsuperuser