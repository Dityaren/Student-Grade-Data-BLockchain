from Test_Block import Block

blockchain = []

genesis_block = Block("Sekarang bulan march tahun 2024", [
                      "Genesis", "0", "0", "0", "0"])

print(genesis_block.block_hash)
