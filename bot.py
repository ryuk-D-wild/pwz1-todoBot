from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Dictionary to store each user's to-do list
user_todos = {}

# Start command
async def start(update: Update, context):
    user = update.effective_user
    await update.message.reply_text(f"Hello, {user.first_name}! This is your simple To-Do bot.")
    await update.message.reply_text("Use /addtodo to add a task, /showtodos to see all tasks, and /cleartodos to clear the list.")

# Add To-Do
async def addtodo(update: Update, context):
    user_id = update.message.from_user.id
    task = " ".join(context.args)

    if not task:
        await update.message.reply_text("Please provide a task to add!")
        return
    
    # Add task to user's to-do list
    if user_id not in user_todos:
        user_todos[user_id] = []
    user_todos[user_id].append(task)
    
    await update.message.reply_text(f"Task added: {task}")

# Show To-Dos
async def showtodos(update: Update, context):
    user_id = update.message.from_user.id
    
    if user_id not in user_todos or not user_todos[user_id]:
        await update.message.reply_text("Your to-do list is empty!")
    else:
        todos = "\n".join([f"{idx + 1}. {todo}" for idx, todo in enumerate(user_todos[user_id])])
        await update.message.reply_text(f"Your tasks:\n{todos}")

# Clear To-Dos
async def cleartodos(update: Update, context):
    user_id = update.message.from_user.id
    
    if user_id in user_todos:
        user_todos[user_id] = []
    await update.message.reply_text("Your to-do list has been cleared!")

# Main function to run the bot
async def main():
    app = ApplicationBuilder().token('7403194359:AAGECbU4FFJXLufcavuk9SHut8GymkkB5hc').build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addtodo", addtodo))
    app.add_handler(CommandHandler("showtodos", showtodos))
    app.add_handler(CommandHandler("cleartodos", cleartodos))

    # Initialize the application
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    # Keep the bot running with a simple infinite loop
    try:
        await asyncio.Future()  # Run forever
    except (KeyboardInterrupt, SystemExit):
        await app.stop()

if __name__ == '__main__':
    import asyncio

async def main():
    try:
        print("Bot is running. Press Ctrl+C to stop.")
        await asyncio.Future()  # Run forever
    except asyncio.CancelledError:
        print("Shutdown requested.")
    finally:
        print("Bot has stopped.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
