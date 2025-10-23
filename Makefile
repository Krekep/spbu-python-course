.PHONY: test test-unit test-integration coverage clean

# Тесты для task4
test:
	python3 scripts/run_tests.py

test-unit:
	python3 scripts/run_tests.py -m "unit"

test-integration:
	python3 scripts/run_tests.py -m "integration"

coverage:
	cd project/task4 && python -m pytest ../../tests/task4/ -v --cov=core --cov=players --cov=strategies --cov-report=html

# Утилиты
check-imports:
	python3 scripts/check_imports.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete

# CI
ci: check-imports test-unit test-integration