# qa_guru_python_9_jenkins

#1. jenkins.autotests.cloud -> New Item -> вводим   НомерПотокаТрехзначный-ЛогинТелеги-НомерУрока, выбираем Freestyle project и энтер
#2. билд
#3. в configuration в Source Code Management выбираем Git
#4. в Repository URL путь к корневому репозиторию в гите
#5. в Branches to build в Branch Specifier меняем ветку с */master на /main если надо
#6. в Build Steps -> Add build step -> Execute shell, где прописываем следующее:
#python -m venv .venv
#source .venv/bin/activate
#pip install -r requirements.txt
#pytest tests/demoqa
#7. Restrict where this project can be run -> python
#8. Post-build Actions -> Add post-build action -> Allure Repost
#9. Apply
#10. Build Now
