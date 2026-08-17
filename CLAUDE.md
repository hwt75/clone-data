# Vault Kinh Dịch — hướng dẫn cho Claude

`claude-source/` là một Obsidian vault tiếng Việt về **Kinh Dịch · Tử Vi Đẩu Số · Nhân tướng học · Hà Lạc · Lục Hào**, hệ thống hóa từ 6 cuốn sách gốc trong `claude-source/nguồn thô/`.

## Quy trình bắt buộc khi trả lời câu hỏi tri thức

1. **Grep `wiki/_Index.md` trước tiên** — chỉ mục một dòng mỗi note (bí danh · nhãn · tóm tắt · các mục). Một lần grep ở đây thay cho việc dò tìm cả vault. Chưa rõ nên tìm từ khóa nào thì đọc bảng nhóm ở đầu chỉ mục.
2. Mở **đúng** note đã xác định. Note lớn (>10 KB) thì grep trong chính nó để lấy đoạn cần, đừng đọc toàn bộ.
3. Chỉ khi chỉ mục không có mới grep toàn `wiki/`.

Đừng bắt đầu bằng Glob/Grep mò trên toàn vault — đó là nguyên nhân trả lời chậm.

## Quy tắc chính xác

- **Chỉ trả lời bằng nội dung có trong `wiki/`.** Kiến thức Kinh Dịch/Tử Vi ngoài vault rất nhiều dị bản; vault này bám theo bản dịch cụ thể đã nêu trong `wiki/Nguồn/`.
- Mọi khẳng định phải **dẫn note nguồn** dạng `[[Tên note]]` để người đọc kiểm chứng được.
- Wiki không có thì **nói thẳng là không có**, kèm gợi ý nguồn nào có thể chứa nó — không suy diễn, không lấp bằng kiến thức chung.
- **Sách nguồn có chỗ trống hoặc tự mâu thuẫn.** Với Tử Vi, thứ tự phân xử đã chốt: chính văn 8 chương → **Toàn Thư** (phụ lục 5–7 của cùng cuốn sách) → mới tới nguồn ngoài, và phải đánh dấu tại chỗ. Xem [[Nguồn tri thức Tử Vi — thứ tự ưu tiên]] trước khi ra ngoài vault.
- Thuật ngữ giữ nguyên tiếng Việt Hán-Việt như trong vault (thoán từ, hào từ, miếu hãm, lưu niên…).

## Bản đồ thư mục

| Hỏi về | Đọc tại |
|---|---|
| Khái niệm nền (âm dương, ngũ hành, hào, Hà Đồ, Lạc Thư, Thập Dực) | `wiki/Khái niệm/` |
| Tám quẻ đơn | `wiki/Bát quái/<Tên>.md` — Càn, Đoài, Ly, Chấn, Tốn, Khảm, Cấn, Khôn |
| Một quẻ trong 64 quẻ | `wiki/64 quẻ/NN Tên đầy đủ.md` — số thứ tự 2 chữ số + tên, ví dụ `03 Thủy Lôi Truân.md` |
| Sao, chính tinh, phụ tinh, miếu hãm | `wiki/Tử Vi Đẩu Số/Sao/` |
| Lập lá số, an sao, 12 cung | `wiki/Tử Vi Đẩu Số/Lá số/` |
| Cách cục, phương pháp luận đoán | `wiki/Tử Vi Đẩu Số/Luận đoán/` |
| Bộ vị trên mặt (mắt, mũi, trán, tai…) | `wiki/Nhân Tướng Học/Bộ vị/` |
| Ngũ hình, tam đình, thần khí, lưu niên | `wiki/Nhân Tướng Học/Khái niệm/`, `.../Lưu niên/` |
| Hà Lạc: lập quẻ đời người | `wiki/Hà Lạc/` |
| Hà Lạc: lời đoán từng quẻ | `wiki/Hà Lạc/Lời đoán/` |
| Lục hào, nạp giáp, dụng thần, ứng kỳ | `wiki/Lục Hào/` |
| Y lý, gieo quẻ, Mai Hoa Dịch Số, Linh Quy Bát Pháp | `wiki/Ứng dụng/` |
| Sách gốc nào nói gì, tình trạng số hóa | `wiki/Nguồn/` |

Ba bản đồ nội dung tổng quan: `wiki/Kinh Dịch — Bản đồ nội dung.md`, `wiki/Tử Vi Đẩu Số/Tử Vi Đẩu Số — Bản đồ nội dung.md`, `wiki/Nhân Tướng Học/Nhân Tướng Học — Bản đồ nội dung.md`.

## Lá số đã lập — `claude-source/Lá số/`

Khu lưu trữ **kết quả áp dụng** (lá số của người cụ thể + luận giải), tách khỏi `wiki/`
là nơi chứa **tri thức**. Nằm ngoài `wiki/` nên không lọt vào `wiki/_Index.md` và không
làm nhiễu tra cứu tri thức, nhưng vẫn trong vault nên wikilink sang wiki vẫn chạy.

Đọc [[_Danh sách lá số]] trước khi lập lá số mới — ở đó có bảng danh sách, quy ước đặt tên
và quy trình 8 bước. Tóm tắt: mỗi lá số là một thư mục `YYYY-MM-DD <Nam|Nữ> <can chi năm>`,
chứa đúng ba tệp **đều mang tiền tố ngày sinh** để tự định danh khi tách khỏi thư mục:

```
Lá số/2001-03-02 Nam Tân Tỵ/
├─ 2001-03-02 Nam Tân Tỵ — Lá số.html   ← bản chính, địa bàn 4×4 tương tác
└─ 2001-03-02 Nam Tân Tỵ — Luận giải.md ← đầu vào, phép tính 23 bước, vận hạn, nhật ký luận
```

### Hỏi về một lá số **đã lập** — đọc theo thứ tự này, đừng đọc cả file

File `— Luận giải.md` lớn và **chỉ tăng** (mục 7 là nhật ký cộng dồn, hiện chiếm ~80% dung lượng).
Đọc cả file là nguyên nhân chính khiến trả lời chậm và tốn. Thứ tự đúng:

1. **`## 7 → ⭐ Kết luận hiện hành`** — bản nén của toàn bộ nhật ký: chân dung, cách cục đã chốt,
   vận hạn, việc cần tránh, và **danh sách cảnh báo đã kiểm là không kích hoạt** (đừng kiểm lại).
   Cuối mục có **mục lục §7** ánh xạ chủ đề → mục A–T.
2. **`## 3 → Bảng tra ngược sao → cung`** — mỗi sao một dòng; grep tên sao thay vì đọc bảng 12 cung.
3. **`## 6. Lưu niên đã an`** — nếu câu hỏi dính tới một năm cụ thể.
4. Chỉ khi cần *vì sao* một kết luận được rút ra, hoặc khi phải xét lại nó, mới mở **đúng mục A–T**
   mà mục lục §7 chỉ tới.

Chưa an sao cho năm được hỏi thì an thêm vào §6 theo [[An sao lưu niên]] trước khi luận.

- **Không xuất PDF** — HTML là định dạng chuẩn; cần bản giấy thì in từ trình duyệt.
- **Không xuất ảnh PNG** — Không cần tạo ảnh PNG.
- **Không sửa tay file HTML.** Phát hiện an sao sai thì sửa quy tắc trong `wiki/` trước,
  rồi lập lại lá số.
- Chép `Lá số/_Mẫu/Mẫu luận giải.md` khi tạo note luận giải mới.
- Ảnh tĩnh chụp bằng Edge headless (`--headless=new --screenshot`), lệnh đầy đủ nằm trong
  [[_Danh sách lá số]].

## Chỉ mục tự cập nhật

`wiki/_Index.md` **sinh tự động** — đừng sửa tay. Một hook `PostToolUse` chạy lại
`.tools/build_index.py` mỗi khi có note trong `wiki/` được Write/Edit, nên chỉ mục luôn khớp
với vault. Sửa note bằng tay ngoài Claude Code thì chạy:

```bash
cd D:/claude/claude-source && PYTHONUTF8=1 python .tools/build_index.py
```

Chỉ mục lấy dữ liệu từ frontmatter, nên **note mới phải có frontmatter** `aliases` + `tags`, một H1, và một đoạn văn mở đầu — đó chính là những gì lọt vào chỉ mục. Thêm thư mục mới thì khai báo trong `GROUP_ORDER` và `GROUP_DESC` của script, nếu không nó bị xếp lạc xuống cuối.

## Khi cần làm OCR hoặc dựng note từ sách scan

Đọc `claude-source/.tools/ocr.md` — quy trình, chất lượng từng công cụ, và các cạm bẫy.
Text OCR thô ở `nguồn thô/_ocr/`, **nằm ngoài `wiki/`** nên không lọt vào phạm vi tìm kiếm tri thức;
đừng trích thẳng từ đó vào wiki mà chưa đối chiếu ảnh trang.

Lịch sử quyết định hạ tầng, ngã cụt đã đi, việc còn tồn đọng: `claude-source/.tools/nhat-ky.md`.

## Ghi chú kỹ thuật của máy này

- Console mặc định cp1252 → chạy Python phải có `PYTHONUTF8=1`.
- `pip install` cần cờ `--user` (máy không có quyền admin).
- Trích text từ PDF: dùng **PyMuPDF (`fitz`)**, không dùng `pdftotext` (làm mất dấu tiếng Việt).
- **Tesseract 5.4.0 đã có** ở `C:\Program Files\Tesseract-OCR\tesseract.exe`; `vie.traineddata` ở `D:\claude\.tessdata` (Tesseract không mở được đường dẫn có dấu tiếng Việt).
