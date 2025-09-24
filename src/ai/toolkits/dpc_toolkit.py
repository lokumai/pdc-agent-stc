from typing import List
from langchain_core.tools import tool
from src.repositories.product_offering_repository import ProductOfferingRepository
from src.repositories.product_specification_repository import ProductSpecificationRepository
from src.repositories.product_characteristic_repository import ProductCharacteristicRepository
from src.repositories.product_price_repository import ProductPriceRepository

import uuid
from src.models.product_catalog import ProductOffering, ProductSpecification, ProductCharacteristic, ProductPrice




@tool
async def upsert_product_offering(offering: ProductOffering) -> dict:
    """
    Save or update a product offering in the database.
    Use this to create or modify product offerings.

    Args:
        offering (ProductOffering): ProductOffering model instance.

    Returns:
        dict: Confirmation message and offering details (including generated id if applicable).
    """
    if not offering.id:
        offering.id = str(uuid.uuid4())
    await ProductOfferingRepository.upsert_offering(offering)
    return {"message": "Product offering upserted.", "offering": offering.model_dump()}


@tool
async def filter_product_offerings(filter_dict: dict) -> list:
    """
    Filter product offerings by any field. Example fields: name, lifecycle_status, target_segments, sales_channels.
    Example filter_dict: {"name": "5g silver"}, {"lifecycle_status": "active"}
    Use this to search for offerings matching specific criteria.

    Args:
        filter_dict (dict): Dictionary of MongoDB query parameters. Use only valid model fields.

    Returns:
        list: List of matching product offerings as dictionaries.
    """
    results = await ProductOfferingRepository.filter_offerings(filter_dict)
    return [r.model_dump() for r in results]



@tool
async def upsert_product_specification(spec: ProductSpecification) -> dict:
    """
    Save or update a product specification in the database.
    Use this to create or modify product specifications.

    Args:
        spec (ProductSpecification): ProductSpecification model instance.

    Returns:
        dict: Confirmation message and specification details (including generated id if applicable).
    """
    if not spec.id:
        spec.id = str(uuid.uuid4())
    await ProductSpecificationRepository.upsert_specification(spec)
    return {"message": "Product specification upserted.", "specification": spec.model_dump()}


@tool
async def filter_product_specifications(filter_dict: dict) -> list:
    """
    Filter product specifications by any field. Example fields: name, lifecycleStatus, brand, isBundle.
    Example filter_dict: {"name": "5g silver"}, {"isBundle": true}
    Use this to search for specifications matching specific criteria.

    Args:
        filter_dict (dict): Dictionary of MongoDB query parameters. Use only valid model fields.

    Returns:
        list: List of matching product specifications as dictionaries.
    """
    results = await ProductSpecificationRepository.filter_specifications(filter_dict)
    return [r.model_dump() for r in results]



@tool
async def upsert_product_characteristic(char: ProductCharacteristic) -> dict:
    """
    Save or update a product characteristic in the database.
    Use this to create or modify product characteristics.

    Args:
        char (ProductCharacteristic): ProductCharacteristic model instance.

    Returns:
        dict: Confirmation message and characteristic details (including generated id if applicable).
    """
    if not char.id:
        char.id = str(uuid.uuid4())
    await ProductCharacteristicRepository.upsert_characteristic(char)
    return {"message": "Product characteristic upserted.", "characteristic": char.model_dump()}


@tool
async def filter_product_characteristics(filter_dict: dict) -> list:
    """
    Filter product characteristics by any field. Example fields: name, characteristicType, isUnique, mandatory.
    Example filter_dict: {"name": "color"}, {"isUnique": true}
    Use this to search for characteristics matching specific criteria.

    Args:
        filter_dict (dict): Dictionary of MongoDB query parameters. Use only valid model fields.

    Returns:
        list: List of matching product characteristics as dictionaries.
    """
    results = await ProductCharacteristicRepository.filter_characteristics(filter_dict)
    return [r.model_dump() for r in results]



@tool
async def upsert_product_price(price: ProductPrice) -> dict:
    """
    Save or update a product price in the database.
    Use this to create or modify product prices.

    Args:
        price (ProductPrice): ProductPrice model instance.

    Returns:
        dict: Confirmation message and price details (including generated id if applicable).
    """
    if not price.id:
        price.id = str(uuid.uuid4())
    await ProductPriceRepository.upsert_price(price)
    return {"message": "Product price upserted.", "price": price.model_dump()}


@tool
async def filter_product_prices(filter_dict: dict) -> list:
    """
    Filter product prices by any field. Example fields: name, priceType, percentage, lifecycleStatus.
    Example filter_dict: {"priceType": "recurring"}, {"percentage": 0.1}
    Use this to search for prices matching specific criteria.

    Args:
        filter_dict (dict): Dictionary of MongoDB query parameters. Use only valid model fields.

    Returns:
        list: List of matching product prices as dictionaries.
    """
    results = await ProductPriceRepository.filter_prices(filter_dict)
    return [r.model_dump() for r in results]


# ============================================================
# ================= LIST TOOLS ===============================
# ============================================================


# # Product Offering List Tool
# @tool
# async def list_product_offerings() -> list:
#     """
#     List all product offerings in the database.
#     Returns:
#         list: List of all product offerings as dictionaries.
#     """
#     results = await ProductOfferingRepository.list_offerings()
#     return [r.model_dump() for r in results]


# # Product Specification List Tool
# @tool
# async def list_product_specifications() -> list:
#     """
#     List all product specifications in the database.
#     Returns:
#         list: List of all product specifications as dictionaries.
#     """
#     results = await ProductSpecificationRepository.list_specifications()
#     return [r.model_dump() for r in results]


# # Product Characteristic List Tool
# @tool
# async def list_product_characteristics() -> list:
#     """
#     List all product characteristics in the database.
#     Returns:
#         list: List of all product characteristics as dictionaries.
#     """
#     results = await ProductCharacteristicRepository.list_characteristics()
#     return [r.model_dump() for r in results]


# # Product Price List Tool
# @tool
# async def list_product_prices() -> list:
#     """
#     List all product prices in the database.
#     Returns:
#         list: List of all product prices as dictionaries.
#     """
#     results = await ProductPriceRepository.list_prices()
#     return [r.model_dump() for r in results]


class DPCToolkit:
    @staticmethod
    def get_tools() -> List:
        """Return a list of upsert, filter, and list tools for product catalog entities."""
        return [
            upsert_product_offering,
            filter_product_offerings,
            upsert_product_specification,
            filter_product_specifications,
            upsert_product_characteristic,
            filter_product_characteristics,
            upsert_product_price,
            filter_product_prices,
            # list_product_offerings,
            # list_product_specifications,
            # list_product_prices,
            # list_product_characteristics,
        ]
