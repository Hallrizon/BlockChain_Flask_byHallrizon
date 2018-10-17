from BlockChainApi import BlockChain
from BlockChainApi import Main

if __name__ == '__main__':
    run = Main(BlockChain)

    run.objects['BlockChain'].check_integrity()
    #run.objects['BlockChain'].write_block(name="Kostik", amount=100, to_whom="Olga")


