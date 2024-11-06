-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2024 at 12:29 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oryxdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` text NOT NULL,
  `product_desc` varchar(500) NOT NULL,
  `product_cost` int(50) NOT NULL,
  `product_category` text NOT NULL,
  `product_image_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_desc`, `product_cost`, `product_category`, `product_image_name`) VALUES
(1, 'Choker Gold Necklace', 'Fashion wear for women', 165, 'Other', 'necklace.jpg'),
(2, 'oppo', 'ram 8 gb', 13000, 'Smartphones', 'laptop.jpeg'),
(3, 'lenovo laptop', 'Memory power 128gb', 50000, 'Electronics', 'laptop2.jpeg'),
(4, 'summer dress', 'cotton', 2500, 'Clothes', 'summerdress.avif'),
(5, 'Gold layered necklace', 'Fashion Jewelry for ladies', 3500, 'Other', 'layerednecklace.jpeg'),
(6, 'Evening Dinner Dress', 'Fashion For Ladies Night Out', 7000, 'Clothes', 'dinnerdress1.jpeg'),
(7, 'Watch for men', 'Fashionable accessories for men', 35000, 'Other', 'watchformen.jpeg'),
(8, 'Gold Ring Set', 'Fashionable jewelry for Ladies', 3000, 'Other', 'ringset.jpg'),
(9, 'Floral Dress', 'Fashion wear for ladies ', 4000, 'Clothes', 'floral dress.jpg'),
(10, 'Pink watch', 'Accessories for ladies', 35000, 'Other', 'pinkwatch.webp'),
(11, 'Kitchen pans set', 'Kitchen Appliances', 25000, 'Utensils', 'panset.jpeg'),
(12, 'Couch Set', 'Furniture Living Room Sofa Set', 250000, 'Other', 'couchset.jpeg'),
(13, 'Off-shoulder Lace Dress', 'Fashion Wear For Ladies', 20000, 'Clothes', 'offshoulderdress.webp'),
(14, 'Phone Cover', 'Cover for phones', 5000, 'Other', 'phonecase.webp'),
(15, 'Sparkly Dress', 'Fashion Wear for Ladies', 25000, 'Clothes', 'sparklydress.jpg'),
(16, 'LED bulb with Bluetooth speaker', 'Music Bluetooth Speaker', 3500, 'Electronics', 'ledbluetoothspeaker.jpg'),
(17, 'JBL Portable Speaker', 'Portable Blue Speaker', 12000, 'Electronics', 'jblspeaker1.jpg'),
(18, '75 inch Samsung Tv', 'Smart Samsung Tv 75 inch', 200000, 'Electronics', '75inchtv.jpg'),
(19, 'LG 75 INCH TV', 'Frameless 75 inch smart tv', 270000, 'Electronics', 'ld75inch.jpg'),
(20, 'Sony 75 inch tv', 'Sony Smart tv 75 inch', 310000, 'Electronics', 'sony75inch.jpg'),
(21, 'Tecno Smartphone', '128gb black in color', 12500, 'Electronics', 'tecnophone.jpg'),
(22, 'Smart Watch', 'Touch screen smart watch', 3000, 'Electronics', 'smartwatch1.jpg'),
(23, 'Ultra 2 Smart watch', 'Touch screen and Bluetooth calls', 3500, 'Electronics', 'ult2smartwatch.jpg'),
(24, 'Modio 5G Tablet', 'Kids Android Tablet', 18000, 'Electronics', 'kidtablet.jpg'),
(25, 'Fluffy fur Coat', 'Coat for Winter For Ladies', 12000, 'Clothes', 'furcoat1.jpeg'),
(26, 'Winter Coat', 'Long sleeved fur coat ', 11500, 'Clothes', 'furcoat2.avif'),
(27, 'White Puffer Jacket', 'Female Long Sleeved and Long Coat', 15500, 'Clothes', 'puffjacket1.jpg'),
(28, 'Denim Jacket', 'Black Cropped Denim Jacket for ladies', 4500, 'Clothes', 'denimcropjkt.jpg'),
(29, 'Wool Jacket', 'Cropped Graphic Jacket for ladies', 4500, 'Clothes', 'woolcropjkt.webp'),
(30, 'Coffee and Tea set', '14pcs of tea cups and plates', 6500, 'Utensils', 'teaset1.jpg'),
(31, 'Pot and pan set', '6 Pots and Pans In Rose Gold', 15050, 'Utensils', 'rosegoldpans.webp'),
(32, 'Pots and Pan Marble Set', 'White in color, 12 pieces', 19650, 'Utensils', 'marblepan.jpeg'),
(33, 'Knife Set', 'Rose gold 9 piece set', 5500, 'Utensils', 'knifeset1.jpg'),
(34, 'Knife Set 16 pieces', 'Titanium coated and blue', 20000, 'Utensils', '16knifeset.webp'),
(35, 'Dinner Set', 'Dinner plates, bowls and spoons', 45000, 'Utensils', 'dinnerwareset.jpg'),
(36, 'Pink Plate Set', 'Plates and Bowls of 6 pieces', 4500, 'Utensils', 'pinkplateset.webp'),
(37, 'Square Plates', 'Black Square Plates Set', 12300, 'Utensils', 'squareplates.jpg'),
(38, 'Porcelain Dinner Set', 'Porcelain 48 set plates', 35400, 'Utensils', 'ceramic dinner set.jpeg'),
(39, 'Infix smart phone', '2 GB RAM+64 GB', 10500, 'Smartphones', 'infinix1.jpg'),
(40, 'Samsung AO5', '128 GB', 15400, 'Smartphones', 'SAMSUNGPHONE1.jpg'),
(41, 'Refurbished OPPO phone', '32 GB', 5500, 'Smartphones', 'OPPO1.jpg'),
(42, 'Itel S23', '128 GB', 18500, 'Smartphones', 'ITELPHONE.jpg'),
(43, 'Tecnopop', '64 GB', 10450, 'Smartphones', 'TECNOPOP.jpg'),
(44, 'Tecno Spark', '128 GB', 15000, 'Smartphones', 'TECNOSPARK.jpg'),
(45, 'Infinix Hot Pro', '256 GB', 30899, 'Smartphones', 'INFINITHOT.jpg'),
(46, 'ITEL S24', '128 GB', 18000, 'Smartphones', 'ITELS24.jpg'),
(47, 'Samsung A51 ', '128 GB', 31500, 'Smartphones', 'SAMSUNGA51.jpg'),
(48, 'Ruby Necklace', 'Fashion wear for ladies', 25500, 'Other', 'RUBYNECKLACE.jpeg'),
(49, 'Locket Necklace', 'Gold Plated for ladies', 2500, 'Other', 'locketneck.webp'),
(50, 'Heart shaped locket', 'Gold for ladies wear', 2500, 'Other', 'heartshapedlock.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `email`, `phone`) VALUES
('farah', '123456789', 'danielsana60@gmail.com', '+254726577467'),
('john', '123456789', 'john@gmail.com', '+254726577467');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
