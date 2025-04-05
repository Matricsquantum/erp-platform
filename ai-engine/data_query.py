# Data query script for SynapseCore ERP
import json
print("Querying mock database...")
mock_db = {"accounts": [{"id": 1, "balance": 1000}, {"id": 2, "balance": 500}]}
print(f"Database Result: {json.dumps(mock_db)}")
