SELECT
    formatDateTime(day, '%Y-%m-%d') AS day,
    sku_id,
    sku,
    price,
    qty
FROM (
    SELECT
        a.day AS day,
        a.sku_id AS sku_id,
        a.sku AS sku,
        a.price AS price,
        b.n_qty AS qty
    FROM (
        SELECT day, sku_id, sku, price
        FROM (
            SELECT DISTINCT(DATE(timestamp)) AS day
            FROM default.demand_orders
        ) x
        CROSS JOIN (
            SELECT DISTINCT(sku_id) AS sku_id, sku, price
            FROM default.demand_orders
        ) y
    ) a
        LEFT JOIN (
        SELECT
            do.sku_id,
            DATE(do.timestamp) AS day,
            sum(do.qty) AS n_qty
        FROM default.demand_orders AS do
            INNER JOIN default.demand_orders_status AS os
            ON do.order_id = os.order_id
        WHERE os.status_id IN (1, 3, 4, 5, 6)
        GROUP BY do.sku_id, day
    ) b
        ON a.sku_id = b.sku_id AND a.day = b.day
    ORDER BY sku_id, day
)
