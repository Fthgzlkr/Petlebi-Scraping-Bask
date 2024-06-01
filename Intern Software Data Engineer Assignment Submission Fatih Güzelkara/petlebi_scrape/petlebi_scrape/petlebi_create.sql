
CREATE DATABASE IF NOT EXISTS petlebidatabase;


USE petlebidatabase;


CREATE TABLE IF NOT EXISTS petlebi (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    product_price DECIMAL(10, 2),
    product_stock VARCHAR(50),
    product_category VARCHAR(255),
    product_brand VARCHAR(100),
    product_url VARCHAR(255),
    product_image VARCHAR(255)
);


INSERT INTO petlebi (product_id, product_name, product_price, product_stock, product_category, product_brand, product_url, product_image) 
VALUES (143, 'Hill''s SCIENCE PLAN Tavuklu Kısırlaştırılmış Kedi Maması 3kg', 1149.00, 'In Stock', 'Kedi Ürünleri > Kedi Maması > Kısırlaştırılmış Kedi Maması', 'Hill''s', 'https://www.petlebi.com/kedi-urunleri/hills-adult-sterilized-kisirlastirilmis-tavuklu-yetiskin-kedi-mamasi-35kg.html', '//images.petlebi.com/v7/_ptlb/up/ecommerce/product/sm_hills-yetiskin-kedi-mamasi-3kg-143168.jpg');
