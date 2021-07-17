import hashlib

class RockCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Micky sends 0.05 RC to Mike"
t2 = "Micky sends 2 RC to Pata"
t3 = "Pata sends 1.5 RC to Sheila"
t4 = "Mike sends 1 RC to Pata"
t5 = "Sheila sends 0.3 RC to Micky"
t6 = "Pata sends 0.25 RC to Micky"

initail_block = RockCoinBlock("Initial String", [t1, t2])
print(initail_block.block_data)
print(initail_block.block_hash)

second_block = RockCoinBlock(initail_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = RockCoinBlock(second_block.block_hash, [t5, t6])
print(third_block.block_data)
print(third_block.block_hash)

