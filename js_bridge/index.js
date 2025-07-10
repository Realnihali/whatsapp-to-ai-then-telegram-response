const { Client, LocalAuth } = require('whatsapp-web.js');
const TelegramBot  = require('node-telegram-bot-api');
const qrcode       = require('qrcode-terminal');

const BOT  = new TelegramBot(process.env.TG_TOKEN);
const CHAT = process.env.TG_CHATID;
const AI   = process.env.AI_JID + "@c.us";      // "+34…@c.us"

const wa = new Client({
  authStrategy: new LocalAuth({ dataPath: './session' }),
  puppeteer: { headless:true, args:['--no-sandbox','--disable-gpu'] }
});

wa.on('qr', qr => {
  qrcode.generate(qr,{small:true});
  BOT.sendPhoto(CHAT,
    `https://api.qrserver.com/v1/create-qr-code/?data=${encodeURIComponent(qr)}&size=300x300`,
    { caption:"📲 Scan to link WhatsApp" });
});
wa.on('ready', ()=>BOT.sendMessage(CHAT,"✅ WhatsApp JS layer ready"));

wa.on('message', async msg=>{
  if(msg.from!==AI && msg.body)
      wa.sendMessage(AI, msg.body);            // forward to AI
});
wa.on('message_create', m=>{
  if(m.from===AI && !m.fromMe)
      BOT.sendMessage(CHAT,`🤖 *AI Reply:*\n${m.body}`,{parse_mode:"Markdown"});
});

wa.initialize();
