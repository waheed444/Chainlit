import chainlit as cl

@cl.on_message     # Use Decorator
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Agent: {message.content}",).send()
    