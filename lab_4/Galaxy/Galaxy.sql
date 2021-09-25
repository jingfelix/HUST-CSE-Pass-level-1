-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 06, 2020 at 09:40 PM
-- Server version: 10.3.22-MariaDB-1
-- PHP Version: 7.3.15-3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Galaxy`
--

-- --------------------------------------------------------

--
-- Table structure for table `AirLineInfo`
--

CREATE TABLE `AirLineInfo` (
  `FlightNum` char(6) NOT NULL,
  `FromCity` char(20) NOT NULL,
  `ToCity` char(20) NOT NULL,
  `DepartureTime` datetime NOT NULL,
  `AriveTime` datetime NOT NULL,
  `AcutalDepTime` datetime NOT NULL,
  `AircraftType` char(10) NOT NULL,
  `BasePrice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `AirLineInfo`
--

INSERT INTO `AirLineInfo` (`FlightNum`, `FromCity`, `ToCity`, `DepartureTime`, `AriveTime`, `AcutalDepTime`, `AircraftType`, `BasePrice`) VALUES
('MU3319', 'WuHan', 'ChengDu', '2020-05-28 13:00:00', '2020-05-28 15:00:00', '2020-05-28 13:00:00', '737', 1200),
('JD5712', 'WuHan', 'ShangHai', '2020-05-28 13:30:00', '2020-05-28 15:30:00', '2020-05-28 13:50:00', '737', 1300),
('MU2508', 'WuHan', 'BeiJing', '2020-05-28 14:30:00', '2020-05-28 16:30:00', '2020-05-28 14:30:00', '320', 1100),
('CZ3368', 'WuHan', 'GuangZhou', '2020-05-28 16:30:00', '2020-05-28 18:30:00', '2020-05-28 16:30:00', '320', 1000),
('CZ6425', 'WuHan', 'KunMing', '2020-05-28 10:30:00', '2020-05-28 12:30:00', '2020-05-28 11:00:00', '737', 1200);

-- --------------------------------------------------------

--
-- Table structure for table `AirTicketDistributor`
--

CREATE TABLE `AirTicketDistributor` (
  `DistributorNumber` smallint(6) NOT NULL,
  `Name` char(25) NOT NULL,
  `PhoneNumber` char(20) NOT NULL,
  `EmailAddress` char(80) NOT NULL,
  `City` char(20) NOT NULL,
  `Level` char(10) NOT NULL,
  `Password` char(100) NOT NULL,
  `LastLoginDate` datetime NOT NULL,
  `ExpiredDate` datetime NOT NULL,
  `AccountLocked` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `AirTicketDistributor`
--

INSERT INTO `AirTicketDistributor` (`DistributorNumber`, `Name`, `PhoneNumber`, `EmailAddress`, `City`, `Level`, `Password`, `LastLoginDate`, `ExpiredDate`, `AccountLocked`) VALUES
(1, 'TianYu', '(86)13299191993', 'tianyu@galaxy.com', 'Wuhan', 'level1', '123456', '2020-05-05 13:17:48', '2022-05-20 13:17:48', 0),
(2, 'WangXiaoya', '(86)13299191892', 'wangxiaoya@galaxy.com', 'BeiJing', 'level1', '123456', '2020-05-04 13:22:15', '2021-05-04 13:22:15', 0),
(3, 'WangHu', '(86)13299191138', 'wanghu@galaxy.com', 'Shanghai', 'level2', '123456', '2020-03-04 13:22:15', '2021-03-04 13:22:15', 0),
(4, 'ZhangMiao', '(86)13299191223', 'zhangmiao@galaxy.com', 'ShenZhen', 'level1', '123456', '2020-04-01 13:22:15', '2021-04-01 13:22:15', 0),
(5, 'LiuMing', '(86)18971178333', 'liuming@galaxy.com', 'ChengDu', 'level1', '123456', '2020-05-01 13:22:15', '2021-05-01 13:22:15', 0),
(6, 'AlanWalker', '(10)1354194150', 'alanwalker@galaxy.com', 'Chicago', 'level1', '123456', '2020-05-02 13:22:15', '2021-05-02 13:22:15', 0);

-- --------------------------------------------------------


--
-- Table structure for table `TicketInfo`
--

CREATE TABLE `TicketInfo` (
  `FlightNum` char(6) NOT NULL,
  `FlightDate` date NOT NULL,
  `PassengerName` char(30) NOT NULL,
  `PhoneNumber` char(20) NOT NULL,
  `Seat` char(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `TicketInfo`
--

INSERT INTO `TicketInfo` (`FlightNum`, `FlightDate`, `PassengerName`, `PhoneNumber`, `Seat`) VALUES
('MU3319', '2020-05-28', 'ZhangSan', '(86)15327190338', '32A'),
('MU3319', '2020-05-28', 'LiSi', '(86)15327190333', '32B'),
('MU3319', '2020-05-28', 'WangWu', '(86)153271902132', '32C'),
('MU3319', '2020-05-28', 'ZhaoLiu', '(86)153271902312', '03A'),
('MU3319', '2020-05-28', 'ZhangYu', '(86)13299191831', '15A'),
('MU3319', '2020-05-28', 'LiWei', '(86)13299191234', '18A'),
('MU3319', '2020-05-28', 'WuJT', '(86)15327190398', '10A'),
('MU3319', '2020-05-28', 'YangYC', '(86)15327190402', '10B'),
('MU3319', '2020-05-28', 'ZhengJX', '(86)153271900422', '10C'),
('MU3319', '2020-05-28', 'GuoJH', '(86)153271900432', '10D'),
('MU3319', '2020-05-28', 'GuYQ', '(86)13299190436', '10E'),
('MU3319', '2020-05-28', 'FanFY', '(86)13299190440', '10F'),
('MU3319', '2020-05-28', 'YueSH', '(86)13299190450', '11A'),
('JD5712', '2020-05-28', 'LiMing', '(86)18971123982', '12A'),
('JD5712', '2020-05-28', 'ZhangKai', '(86)12671123982', '12C'),
('JD5712', '2020-05-28', 'XiaoTian', '(86)17871123564', '14A'),
('JD5712', '2020-05-28', 'FengChen', '(86)17878741462', '19C');

--
-- Indexes for dumped tables
--



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
