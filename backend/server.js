require('dotenv').config();
const express = require('express');
const cors = require('cors');
const connectDB = require('./config/db');

const app = express();

// 连接数据库
connectDB();

// 中间件
app.use(cors());
app.use(express.json());

// 路由
app.use('/api', require('./routes/auth'));

// 改用3000端口
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`服务器运行在端口 ${PORT}`);
}); 