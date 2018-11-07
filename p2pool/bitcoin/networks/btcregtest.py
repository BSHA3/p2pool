import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'fabfb5da'.decode('hex')
P2P_PORT = 18444
ADDRESS_VERSION = 111
RPC_PORT = 28334
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help())
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//150
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'rBSHA3'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'BSHA3') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/BSHA3/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bsha3'), 'bitcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = '#'
ADDRESS_EXPLORER_URL_PREFIX = '#'
TX_EXPLORER_URL_PREFIX = '#'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 1e8
