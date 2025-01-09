def format_db(data):
  return {
    "product_id": data.product_id,
    "image_url": data.image_url,
    "product_name": data.product_name,
    "price": data.price,
    "brand": data.brand,
    "status": data.status,
    "created_at": data.created_at,
    "updated_at": data.updated_at,
  }
