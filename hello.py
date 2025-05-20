import chainlit as cl

@cl.on_message     # Use Decorator
async def main(message: cl.Message):

    # Send a response back to the user
    await cl.Message(
        content=f"Response: {message.content}",).send()
    