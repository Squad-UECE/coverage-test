coverage:
	@pytest --cov-config=.coveragerc --cov=coverage_study tests
	@coverage-badge -f -o coverage.svg