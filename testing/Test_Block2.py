from Test_Block import Block

blockchain = []
genesis_block = Block("Sekarang bulan march tahun 2024", [
                      "FIRST BLOCK", "1", "1", "1", "1"])
second_block = Block(genesis_block.block_hash, [
                     "SECOND BLOCK", "1", "1", "1", "1"])
third_block = Block(second_block.block_hash, [
                      "THIRD BLOCK", "1", "1", "1", "1"])

print("FIRST BLOCK")
print(genesis_block.block_hash)
print("SECOND BLOCK")
print(second_block.block_hash)
print("THIRD BLOCK")
print(third_block.block_hash)
