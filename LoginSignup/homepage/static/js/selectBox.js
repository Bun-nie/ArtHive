'use strict'
{
    const selectBox={
        caches: {},
        init: function(id){
            const box = document.getElementById(id);
            selectBox.cache[id] = [];
            const cache = selectBox.cache[id];
            for(const node of box.options){
                cache.push({value: node.value, text: node.text, displayed: 1});
            }
        },
        redisplay: function(id){
            //repopulate
            const box = document.getElementById(id);
            box.innerHTML = '';
            for(const node of selectBox.cache[id]){
                if(node.displayed){
                    const new_options = new Option(node.text, node.value, false, false);
                    //show tip on hover
                    new_options.title = node.text;
                    box.appendChild(new_options);
                }
            }
        },
        filter: function(id, text){
            //display choices containing all words in text
            const tokens = text.toLowerCase().split(/\s+/);
            for(const node of selectBox.cache[id]){
                node.displayed = 1;
                const node_text = node.text.toLowerCase();
                for(const token of tokens){
                    if(node_text.indexOf(token) === -1){
                        node.displayed = 0;
                        break; //if first token is not found
                    }
                }
            }
            selectBox.redisplay(id);
        },
        delete_from_cache: function(id, value){
            let delete_index = null;
            const cache = selectBox.cache[id];
            for(const [i, node] of cache.entries()){
                if(node.value === value){
                    delete_index = i;
                    break;
                }
            }
            cache.splice(delete_index, 1);
        },
        add_to_cache: function(id, option){
            selectBox.cache[id].push({value:option.value, text: option.text, displayed: 1});
        },
        cache_contains: function(id, value){
            //if item is in the cache
            for(const node of selectBox.cache[id]){
                if(node.value === value){
                    return true;
                }
            }
            return false;
        },
        move: function(from, to){
            const from_box = document.getElementById(from);
            for(const op of from_box.options){
                const option_value = option.value;
                if(option.selected && selectBox.cache_contains(from, option_value)){
                    selectBox.add_to_cache(to, {value:option_value, text: option.text, displayed: 1});
                    selectBox.delete_from_cache(from, option_value);
                }
            }
            selectBox.redisplay(from);
            selectBox.redisplay(to);
        },
        move_all: function(from, to){
            const from_box = document.getElementById(from);
            for(const option of from_box.options){
                const option_value = option.value;
                if(selectBox.cache_contains(from, option_value)){
                    selectBox.add_to_cache(to, {value:option_value, text: option.text, displayed: 1});
                    selectBox.delete_from_cache(from, option_value);
                }
            }
            selectBox.redisplay(from);
            selectBox.redisplay(to);
        },
        sort: function(id){
            selectBox.cache[id].sort(function(a, b){
                a = a.text.toLowerCase();
                b = b.text.toLowerCase();
                if(a > b) return 1;
                if(a < b) return -1;

                return 0;
            });
        },
        select_all: function(id){
            const box = document.getElementById(id);
            for(const option of box.options){
                option.selected = true;
            }
        }
    }; //end of function

    window.selectBox = selectBox;
} //end of js