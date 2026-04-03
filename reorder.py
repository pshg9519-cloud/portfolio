import io, sys

file_path = r'c:\Users\pshg9\Desktop\ワードプレス\bodako\portfolio\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read().replace('\r\n', '\n')

def get_block(text, start_str, end_str):
    s = text.find(start_str)
    if s == -1: print(f"Not found: {start_str}"); sys.exit(1)
    e = text.find(end_str, s)
    if e == -1: print(f"Not found: {end_str}"); sys.exit(1)
    return text[s:e]

yt = get_block(text, '            <!-- YouTube Videos -->', '            <!-- Nico Nico Douga -->')
nico = get_block(text, '            <!-- Nico Nico Douga -->', '            <!-- Note -->')
note = get_block(text, '            <!-- Note -->', '            <!-- LINE Stamp -->')
line = get_block(text, '            <!-- LINE Stamp -->', '            <!-- X / Twitter Posts -->')
x_manga = get_block(text, '            <!-- X / Twitter Posts -->', '        </div>\n    </section>')

x_abs_content = '''            <!-- X / Twitter Posts (Abstinence Account) -->
            <div id="x-abstinence" class="mb-20 scroll-mt-24">
                <div class="flex items-center justify-center space-x-3 mb-8">
                    <i class="fab fa-x-twitter text-gray-900 text-3xl"></i>
                    <h4 class="text-2xl font-bold text-gray-900 whitespace-nowrap">もうひとつのXアカウント</h4>
                </div>
                <div class="max-w-4xl mx-auto">
                    <div class="bg-white rounded-[2rem] p-8 md:p-12 shadow-md border border-gray-100 hover:shadow-lg transition-all duration-300 relative overflow-hidden">
                        <i class="fab fa-x-twitter text-gray-50 text-9xl absolute -bottom-4 -right-4 md:-bottom-10 md:-right-10 opacity-80 transform -rotate-12 pointer-events-none"></i>
                        <div class="relative z-10">
                            <p class="text-gray-700 leading-relaxed text-base md:text-lg mb-8 text-center max-w-2xl mx-auto font-medium">
                                「yuzuyuzu」名義で、自分の実生活でのアルコールに関する問題やASDと向き合う日々をなるべく楽しく発信する別アカウントも運営しています。<br class="hidden md:block mt-2">
                                こちらのアカウントでも<strong class="text-gray-900 font-bold border-b-2 border-green-400 opacity-90 pb-0.5">「三丁目のボダ子さんノンアル編」</strong>など、日々のリアルな葛藤をクスッと笑える漫画等で発信していますので、ご興味を持たれた方はぜひ覗いてみてください！
                            </p>
                            <div class="text-center">
                                <a href="https://twitter.com/Yuzuyuz82578822" target="_blank" rel="noopener noreferrer"
                                    class="inline-flex items-center justify-center px-10 py-4 text-white bg-gray-900 hover:bg-gray-800 rounded-full font-bold text-lg transition-transform hover:-translate-y-1 shadow-[0_4px_14px_0_rgba(0,0,0,0.39)] hover:shadow-[0_6px_20px_rgba(0,0,0,0.23)]">
                                    <i class="fab fa-x-twitter text-2xl mr-3"></i> 依存症・ASDアカウントを見る
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>\n\n'''

header_part = text[:text.find('            <!-- YouTube Videos -->')]
footer_part = text[text.find('    <!-- About Section -->'):]

new_full_text = header_part + x_manga + x_abs_content + line + yt + nico + note + "        </div>\n    </section>\n\n    " + footer_part

# Write back in the same platform-agnostic way
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_full_text)

print("success")
