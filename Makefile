install:
	@poetry install
requirements:
	@poetry export -o requirements.txt --without-hashes --dev
coverage:
	@pytest --cov-config=.coveragerc --cov=coverage_study --cov-fail-under=100 --no-cov-on-fail tests
	@coverage-badge -f -o coverage.svg