CREATE SCHEMA `twitterdb` ;

CREATE TABLE `tweet` (
    `tweet_id` int unsigned NOT NULL AUTO_INCREMENT,
    `user_id` int DEFAULT NULL,
    `tweet_ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    `tweet_text` varchar(140) DEFAULT NULL,
    PRIMARY KEY (`tweet_id`)
  );

CREATE TABLE `follows` (
    `user_id` int DEFAULT NULL,
    `follows_id` int DEFAULT NULL
  );

