require('dotenv').config();
const mongoose = require('mongoose');

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.MONGODB_URI);
        console.log('MongoDB Atlas 连接成功');
    } catch (err) {
        console.error('MongoDB 连接失败:', err.message);
        process.exit(1);
    }
};

module.exports = connectDB;