
extensions = .md .pdf .html .tex

dest = $(addprefix out/demo,$(extensions))


all: $(dest)


$(filter out/demo.%,$(dest)): demo.md

out/%:
	@if [ ! -d $(dir $@) ]; then mkdir -p $(dir $@); fi
	pandoc $^ -s --filter pandoc-comments -o $@


restore: clean
	for num in "" ; do \
      for ext in $(extensions) ; do \
        git checkout out/demo$$num$$ext ; \
      done ; \
    done

.PHONY: clean

clean:
	rm -rf out
