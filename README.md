CaesarBot
===

Telegram bot who can do a lot of things, such as:

- 💸 budget controlling and analyzing
- ⚽ sport drills tracker and routines scheduler
- 🍲 meal scheduler and dish suggester
- 📑 integration with todoist to create/change/review tasks and grab statistics
- 📗 integration with google sheets to modify and analyze tracker-tables (such as everyday checklist)
- #️⃣ a lot more designing...

---

## Roadmap

Working process separated into Sprints (1 week), each with tasks and end-goal.

*Keys:*     
🔶 - main purpose of a sprint   
🏁 - sprint has finished     
⭐ - current sprint      
✔️ - task done   
⚠️ - task has done, but some planned functions have been discarded   
🏃️ - work on task is in progress   
⏲️ - task has been moved to next sprint because of deadline breaking      
❌ - task has been rejected because of changed conditions   

---

### ⭐ Sprint 2 - Finance-bot Refactoring (2021.06.14 - 2021.06.20)

&nbsp;&nbsp;&nbsp;&nbsp;*🔶 Refine telegram-finance-bot to my code style and english language*

- 🏃 Implement sqlalchemy functionality with alembic migrations
- Implement simple notebook functionality (possibility to write notes which will be saved in db)
- Build main file structure by refactoring telegram-finance-bot 
- Configure home first server to host bot with notebook functionality
- Refactor, translate to english and polish telegram-finance-bot
- Deploy minimal-valuable-product (same refactored functions of telegram-finance-bot) to home server for permanent testing

### 🏁 Sprint 1 - Minimal deploy (2021.06.07 - 2021.06.13)

&nbsp;&nbsp;&nbsp;&nbsp;*🔶 Run MVP notebook bot for testing and defining future development*

- ✔️ Design general development plan and detailed one for the first sprint 
- ✔️ Perform first-view rebuild of telegram-finance-bot for future considerations and development
- ⏲️ Implement simple blocknote functionality (possibility to write notes which will be saved in db)

---

## References

1. [telegram-finance-bot](https://github.com/alexey-goloburdin/telegram-finance-bot) | prototype of the budget core and a server controller reference

2. [aiogram-docs](https://docs.aiogram.dev/en/latest/) | telegram bots API documentation source

3. [VScode-VIM Roadmap](https://github.com/VSCodeVim/Vim/blob/master/ROADMAP.md) | inspiration with Keys designing for roadmap




