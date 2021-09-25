-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- 主机： localhost:3306
-- 生成日期： 2021-06-07 07:23:20
-- 服务器版本： 10.5.8-MariaDB-3
-- PHP 版本： 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `Galaxy`
--

-- --------------------------------------------------------

--
-- 表的结构 `AirTicketDistributor`
--

CREATE TABLE `AirTicketDistributor` (
  `DistributorNumber` smallint(6) NOT NULL,
  `Name` char(25) NOT NULL,
  `PhoneNumber` char(40) NOT NULL,
  `EmailAddress` char(80) NOT NULL,
  `City` char(20) NOT NULL,
  `Level` char(10) NOT NULL,
  `Password` char(100) NOT NULL,
  `LastLoginDate` datetime NOT NULL,
  `ExpiredDate` datetime NOT NULL,
  `AccountLocked` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `AirTicketDistributor`
--

INSERT INTO `AirTicketDistributor` (`DistributorNumber`, `Name`, `PhoneNumber`, `EmailAddress`, `City`, `Level`, `Password`, `LastLoginDate`, `ExpiredDate`, `AccountLocked`) VALUES
(1, 'TianYu', 'DD1A274E0D2AAC766F9F8991FDD3D13D', 'tianyu@galaxy.com', 'Wuhan', 'level1', 'e10adc3949ba59abbe56e057f20f883e', '2020-05-05 13:17:48', '2022-05-20 13:17:48', 0),
(2, 'WangXiaoya', 'C68B18084FDC989EEE02319FA706912A', 'wangxiaoya@galaxy.com', 'BeiJing', 'level1', 'e10adc3949ba59abbe56e057f20f883e', '2020-05-04 13:22:15', '2021-05-04 13:22:15', 0),
(4, 'ZhangMiao', '53094FFDC0FC6988AC047A7F72BE7B4A', 'zhangmiao@galaxy.com', 'ShenZhen', 'level1', 'e10adc3949ba59abbe56e057f20f883e', '2020-04-01 13:22:15', '2021-04-01 13:22:15', 0),
(5, 'LiuMing', '1BF117ADB7B509123BC14A692FE79672', 'liuming@galaxy.com', 'ChengDu', 'level1', 'e10adc3949ba59abbe56e057f20f883e', '2020-05-01 13:22:15', '2021-05-01 13:22:15', 0),
(6, 'AlanWalker', '7BB076C3C5492A8ADD5F784E05FF4AC9', 'alanwalker@galaxy.com', 'Chicago', 'level1', 'e10adc3949ba59abbe56e057f20f883e', '2020-05-02 13:22:15', '2021-05-02 13:22:15', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
