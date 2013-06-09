build: get_full_dictionary get_simple_dictionary clean 

get_full_dictionary: mkdir 
	# Download Wiktionary full English dictionary from Wikimedia
	rm wiktionary_english_full
	wget --progress=dot -O- "http://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-all-titles-in-ns0.gz" | gunzip > tmp/wiktionary_english_full
	#cat /tmp/full | gunzip > tmp/wiktionary_english_full
	egrep "^[a-z]{1,11}$$" tmp/wiktionary_english_full > wiktionary_english_full

get_simple_dictionary: mkdir
	# Download Wiktionary list of most common English words from Wikimedia
	rm wiktionary_english_most_common
	wget --progress=dot -O- "http://simple.wiktionary.org/wiki/Wiktionary:General_Service_List" > tmp/wiktionary_english_most_common
	#cat /tmp/common > tmp/wiktionary_english_most_common
	grep -o "wiki\/[a-z][a-z]*" tmp/wiktionary_english_most_common | cut -f 2 -d'/' | sort > wiktionary_english_most_common 

mkdir:
	rm -rf tmp
	mkdir -p tmp

clean:
	rm -rf tmp
