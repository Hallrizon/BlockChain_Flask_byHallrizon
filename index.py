from BlockChainApi import BlockChain
from BlockChainApi import Main

if __name__ == '__main__':
    run = Main(BlockChain)

    #run.objects['BlockChain'].check_integrity()
    run.objects['BlockChain'].audit_name_blocks_desc()
    #run.objects['BlockChain'].write_block(name="Olga", amount=5, to_whom="Oksana")


