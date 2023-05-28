from dataclasses import dataclass


@dataclass(frozen=True)
class FieldsEnum:
    ACTION: str = "&action="
    ADDRESS: str = "&address="
    API_KEY: str = "&apikey="
    BLOCK_TYPE: str = "&blocktype="
    BLOCKNO: str = "&blockno="
    BLOCKS: str = "blocks"  #
    BOOLEAN: str = "&boolean="
    CLIENT_TYPE: str = "&clienttype="
    CLOSEST: str = "&closest="
    CONTRACT_ADDRESS: str = "&contractaddress="
    DATA: str = "&data="
    END_BLOCK: str = "&endblock="
    END_DATE: str = "&enddate="
    FROM_BLOCK: str = "&fromBlock="
    FROM: str = "&from="
    GAS_PRICE: str = "&gasPrice="
    GAS: str = "&gas="
    HEX: str = "&hex="
    INDEX: str = "&index="
    MODULE: str = "module="
    OFFSET: str = "&offset="
    PAGE: str = "&page="
    POSITION: str = "&position="
    PREFIX: str = "https://api.arbiscan.io/api?"
    SORT: str = "&sort="
    START_BLOCK: str = "&startblock="
    START_DATE: str = "&startdate="
    SYNC_MODE: str = "&syncmode="
    TAG: str = "&tag="
    TIMESTAMP: str = "&timestamp="
    TO_BLOCK: str = "&toBlock="
    TO: str = "&to="
    TOPIC_0_1_OPR: str = "&topic0_1_opr="
    TOPIC_0_2_OPR: str = "&topic0_2_opr="
    TOPIC_0_3_OPR: str = "&topic0_3_opr="
    TOPIC_0: str = "&topic0="
    TOPIC_1_2_OPR: str = "&topic1_2_opr="
    TOPIC_1_3_OPR: str = "&topic1_3_opr="
    TOPIC_1: str = "&topic1="
    TOPIC_2_3_OPR: str = "&topic2_3_opr="
    TOPIC_2: str = "&topic2="
    TOPIC_3: str = "&topic3="
    TXHASH: str = "&txhash="
    VALUE: str = "&value="
