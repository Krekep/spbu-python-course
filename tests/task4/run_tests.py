#!/usr/bin/env python3
"""
Скрипт для запуска тестов в CI/CD окружении
"""
import pytest
import sys
import os


def main():
    """Основная функция запуска тестов"""
    print("🎰 Starting Blackjack Tests in CI/CD...")
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")

    # Добавляем пути для импортов с учетом структуры проекта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # spbu-python-course/

    # Пути к коду и тестам
    task4_code_dir = os.path.join(project_root, "project", "task4")
    task4_tests_dir = os.path.join(project_root, "tests", "task4")

    print(f"Code directory: {task4_code_dir}")
    print(f"Tests directory: {task4_tests_dir}")

    # Добавляем пути в sys.path
    sys.path.insert(0, task4_code_dir)
    sys.path.insert(0, task4_tests_dir)

    # Аргументы для pytest
    pytest_args = [
        task4_tests_dir,  # Папка с тестами
        "-v",  # Подробный вывод
        "--tb=short",  # Короткий traceback
        "--color=yes",  # Цветной вывод
        "--strict-markers",  # Строгая проверка маркеров
    ]

    # Добавляем маркер, если указан
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--marker", help="Run tests with specific marker")
    args = parser.parse_args()

    if args.marker:
        pytest_args.extend(["-m", args.marker])

    print(f"Pytest arguments: {pytest_args}")

    # Запускаем pytest
    exit_code = pytest.main(pytest_args)

    print(f"🎰 Tests completed with exit code: {exit_code}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
