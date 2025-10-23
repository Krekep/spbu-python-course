#!/usr/bin/env python3
"""
Скрипт для проверки импортов в CI
"""
import sys
import os

def check_imports():
    """Проверяем, что все модули могут быть импортированы"""
    print("🔍 Checking imports...")
    
    # Добавляем пути для импортов с учетом структуры проекта
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)  # spbu-python-course/
    task4_dir = os.path.join(project_root, "project", "task4")
    
    sys.path.insert(0, task4_dir)
    
    modules_to_check = [
        'core.card',
        'core.deck', 
        'core.hand',
        'core.game',
        'players.player',
        'players.bot',
        'players.human', 
        'players.dealer',
        'strategies.conservative',
        'strategies.aggressive',
        'strategies.basic',
    ]
    
    success = True
    for module_name in modules_to_check:
        try:
            __import__(module_name)
            print(f"✅ {module_name}")
        except ImportError as e:
            print(f"❌ {module_name}: {e}")
            success = False
    
    return success

if __name__ == "__main__":
    if check_imports():
        print("🎉 All imports successful!")
        sys.exit(0)
    else:
        print("💥 Some imports failed!")
        sys.exit(1)