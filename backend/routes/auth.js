const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');

// 注册路由
router.post('/register', async (req, res) => {
    try {
        const { username, email, password } = req.body;

        // 检查用户是否已存在
        let user = await User.findOne({ email });
        if (user) {
            return res.status(400).json({ error: '该邮箱已被注册' });
        }

        user = await User.findOne({ username });
        if (user) {
            return res.status(400).json({ error: '该用户名已被使用' });
        }

        // 创建新用户
        user = new User({
            username,
            email,
            password
        });

        // 密码加密
        const salt = await bcrypt.genSalt(10);
        user.password = await bcrypt.hash(password, salt);

        // 保存用户
        await user.save();

        // 创建 JWT token
        const payload = {
            user: {
                id: user.id
            }
        };

        jwt.sign(
            payload,
            'your-jwt-secret', // 在生产环境中应该使用环境变量
            { expiresIn: '1h' },
            (err, token) => {
                if (err) throw err;
                res.json({ token });
            }
        );
    } catch (err) {
        console.error(err.message);
        res.status(500).json({ error: '服务器错误' });
    }
});

// 登录路由
router.post('/login', async (req, res) => {
    try {
        const { email, password } = req.body;

        // 检查用户是否存在
        let user = await User.findOne({ email });
        if (!user) {
            return res.status(400).json({ error: '用户不存在' });
        }

        // 验证密码
        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) {
            return res.status(400).json({ error: '密码错误' });
        }

        // 创建 JWT token
        const payload = {
            user: {
                id: user.id
            }
        };

        jwt.sign(
            payload,
            'your-jwt-secret', // 在生产环境中应该使用环境变量
            { expiresIn: '1h' },
            (err, token) => {
                if (err) throw err;
                res.json({ token });
            }
        );
    } catch (err) {
        console.error(err.message);
        res.status(500).json({ error: '服务器错误' });
    }
});

module.exports = router; 