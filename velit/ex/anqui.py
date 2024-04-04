def inch_swap_usdc(privatekey):
    """Inch swap USDC to USDT.

    Args:
        privatekey (str): Private key.
    """

    # Create a new instance of the client.
    client = inch.Client()

    # Get the current gas price.
    gas_price = client.get_gas_price()

    # Create a new transaction.
    tx = inch.Transaction(
        # The address of the sender.
        sender="0x0000000000000000000000000000000000000000",
        # The address of the recipient.
        recipient="0x0000000000000000000000000000000000000000",
        # The amount of USDC to swap.
        amount=1000000000000000000,
        # The address of the USDC token.
        token_address="0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
        # The address of the USDT token.
        to_token_address="0xdac17f958d2ee523a2206206994597c13d831ec7",
        # The maximum amount of USDT to receive.
        max_to_amount=1000000000000000000,
        # The gas price.
        gas_price=gas_price,
        # The gas limit.
        gas_limit=200000,
        # The nonce.
        nonce=0,
    )

    # Sign the transaction.
    tx.sign(privatekey)

    # Send the transaction.
    client.send_transaction(tx)

    # Wait for the transaction to be mined.
    client.wait_for_transaction(tx.hash)

    # Print the transaction hash.
    print(tx.hash)
