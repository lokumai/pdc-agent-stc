# TMF620 product catalog agent chat ui


MVP: No security, no logging, no best-practice, fully vibe-coding. (PoC project for starting a new project)

## LLM
* gpt-oss-20B 
* gemma 12b **
* deepseek R1 8b ****
* qwen3 1.7B 
* qwen3 4B ***
* qwen3 8B ****
* nemotron-nano-9b-v2 ***

LLM Environment:
* Mac M3 chip 18Ram
* LMStudio / ollama


## UI
-- React

    ### PageList
    left side panel:
    * chat
    * history
    * todo

    right side panel:
    * product offering model cards (offering, specification, characteristic, price) model details and status (draft, inprogress, completed)

---

## Backend
* python 
* fastapi
* langchain
* langgraph-react-agent
* langsmith (debugging/tracing)

---

## Database
MongoDB
- chat_completions (chat, message, thread_id, todo-list, )
- product_specification
- product_characteristic
- product_price
- product_offering
- product_catalog_model_status
- agent_memory
- application_logs

---

## API
* POST /chat-completions
* GET /chat-histories

Get Product catalog model list [offering, specification, characteristic, price, etc..]
* GET /product-catalog-models
  
---

Get Product catalog model status and details
* GET /product-catalog-models/{model_name=offering}/details
```json
{
    "completion_status": "inprogress",
    "progress": 80,
    "details": {
        "offering": {
            "name": "5g silver",
            "description": "5g silver description",
            "lifecycle_status": "active",
            "valid_from": "2025-01-01",
            "valid_to": "2025-12-31",
            "target_segments": ["consumer", "business"],
            "sales_channels": ["online", "offline"],
        }
    }
}
```

* GET /product-catalog-models/{model_name=specification}/details
```json
{
    "completion_status": "inprogress",
    "progress": 70,
        "specification": {
            "id": "string",
            "version": "string",
            "@baseType": "string",
            "@schemaLocation": "string",
            "@type": "string",            
            "brand": "string",
            "description": "string",
            "isBundle": true,
            "lastUpdate": "2025-09-18T13:54:26.590Z",
            "lifecycleStatus": "string",
            "name": "string",
            "productNumber": "string",
        }
}
```

* GET /product-catalog-models/{model_name=characteristic}/details
```json
{
    "completion_status": "inprogress",
    "progress": 60,
    "characteristic": {
            "id": "string",
            "@baseType": "string",
            "@schemaLocation": "string",
            "@type": "string",
            "characteristicType": "string",
            "configurable": true,
            "isModifiable": true,
            "description": "string",
            "extensible": true,
            "isUnique": true,
            "isVisible": true,
            "mandatory": true,
            "maxCardinality": 0,
            "minCardinality": 0,
            "name": "string",
            "productCharacteristicValue": [
                {
                "valueType": "string",
                "value": "string",
                "unitOfMeasure": "string",
                "valueFrom": "string",
                "valueTo": "string",
                "rangeInterval": "string",
                "regex": "string",
                "@type": "string",
                "@schemaLocation": "string",
                "isDefault": true
                }
            ],
            "regex": "string",
            "revision": 0,
            "valueSchemaLocation": "string",
            "valueType": "string"
    }
}
```
* GET /product-catalog-models/{model_name=price}/details
```json
{
    "completion_status": "inprogress",
    "progress": 60,
        "price": {
            "id": "string",
            "version": "string",
            "description": "string",
            "isBundle": true,
            "lastUpdate": "2025-09-18T13:55:44.267Z",
            "lifecycleStatus": "string",
            "name": "string",
            "percentage": 0.1,
            "priceType": "string",
            "recurringChargePeriodLength": 0,
            "recurringChargePeriodType": "string",            
            "@baseType": "string",
            "@schemaLocation": "string",
            "@type": "string",            
            "recurringChargePeriodCount": 0,
            "advancedPricingMethod": "string",
            "pricingCategory": "string",
            "salesTime": "string"
        }
}
```

## MCP Server (Model Context Protocol Server)
**No need MCP Server for MVP!!!**

---

## Backend Agent

Use native tools for MVP.
```python


#region Save Tools
@tool
def save_pc(param: SimplePCEdit)-> SimplePCResponse:
    """
    Save product catalog model to database
    """
    
    do_something()
    #------------------------
    #  * give an instruction
    #  * role
    #  * rules
    #  * tmf-rules
    #  * restrictions
    #  * goal
    #  * expected output
    #  * example
    #------------------------
    do_something()

    dbModel = SimplePCModel

    mongodb.insert(dbModel)

    return dbModel


@tool
def save_pp():
    """
    Save product price to database
    """
    pass

@tool
def save_ps():
    """
    Save product specification to database
    """
    pass

@tool
def save_po():
    """
    Save product offering to database
    """
    pass
#endregion Save Tools

#region Filter Tools
@tool
def filter_ps():
    """
    Filter product specification from database
    """
    pass

@tool
def filter_po():
    """
    Filter product offering from database
    """
    pass

#endregion Filter Tools


```